import json
import logging
import os

import pytest
from datetime import date, timedelta
import random
from config import BASE_URL
from e2e_tests.constants.test_data import OFFER_DETAILS_FILE, VALIDATE_OFFER_DATA_FILE
from e2e_tests.pages.conftest import navigate_to_offer
from e2e_tests.pages.landing_page import wait_for_search_results, get_all_offers
from e2e_tests.pages.request_to_book_page import get_final_fee_text, get_final_total_text, get_final_accommodation_text


@pytest.fixture(scope="session")
def home_page(browser):
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()


@pytest.fixture(scope='function')
def after_test(home_page):
    yield
    home_page.goto(BASE_URL)

@pytest.fixture
def get_random_dates():
    today = date.today()
    max_days = 30

    check_in_offset = random.randint(0, max_days - 2)  # leave at least 1 day for checkout
    check_out_offset = random.randint(check_in_offset + 1, max_days)

    check_in = today + timedelta(days=check_in_offset)
    check_out = today + timedelta(days=check_out_offset)
    return [check_in.strftime('%Y-%m-%d'), check_out.strftime('%Y-%m-%d')]

def find_the_best_offer(page):
    if not wait_for_search_results(page):
        return False
    big_rate = 0
    cheapest_price = -1
    best_offer = 0
    cards = get_all_offers(page)
    for i in range(cards.count()):
        card = cards.nth(i)
        rating = card.locator("span", has_text="out of 5")
        total = card.locator("span[aria-hidden='true']", has_text="total")
        if rating.count() > 0:
            new_rate  = float(rating.first.text_content().split()[0])
            new_price = int(total.first.text_content().translate(str.maketrans('', '', '₪, total')).strip())
            if big_rate == 0:
                big_rate  = new_rate
                cheapest_price = new_price
                best_offer = card
            elif new_rate > big_rate:
                big_rate = new_rate
                cheapest_price = new_price
                best_offer = card
            elif big_rate == new_rate:
                if cheapest_price > new_price:
                    cheapest_price = new_price
                    best_offer = card
    return best_offer


def parse_and_log_the_data_to_file(offer):
    url_element = offer.locator('[itemprop="url"]')
    raw_url = url_element.get_attribute('content')
    rate_and_reviews = offer.locator("span", has_text="out of 5").first.text_content().split()
    offer_data = {
        'url': raw_url,
        'item_name': offer.locator("[data-testid='listing-card-name']").text_content(),
        'price_total':  offer.locator("span", has_text=" total").first.text_content().split()[0].replace("₪", ""),
        "rate": rate_and_reviews[0],
        "reviews": rate_and_reviews[6]}
    log_the_result(offer_data, OFFER_DETAILS_FILE)
    return offer_data


def log_the_result(offer, file_name):
    os.makedirs("temp", exist_ok=True)
    with open(f"temp/{file_name}.json", "w", encoding="utf-8") as f:
        json.dump(offer, f)


def validate_the_offer_match_json_data(page, offer, offer_parsed_data, logger):
    navigate_to_offer(page, offer)
    for key, value in offer_parsed_data.items():
        if key == 'url':
            continue
        locator = page.locator(f"text={value}").first
        if locator.count() == 0:
            logger.info(f"Validation failed: '{value}' not visible for key '{key}'")
            return False
    return True


@pytest.fixture(scope="function")
def logger(request):
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    return logger

def parse_and_log_final_data_of_offer(page):
    fee = get_final_fee_text(page)
    total = get_final_total_text(page)
    acc = get_final_accommodation_text(page)
    log_the_result( {'fee': fee, 'total': total, 'accommodation': acc}, VALIDATE_OFFER_DATA_FILE )
