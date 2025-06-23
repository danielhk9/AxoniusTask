from e2e_tests.pages.search_page import SearchPage
from e2e_tests.constants.test_data import LOCATION, PHONE_NUMBER
from e2e_tests.pages.reservation_page import ReservationPage
from e2e_tests.pages.results_page import ResultsPage
from e2e_tests.utils.constants import OFFER_DETAILS_FILE, VALIDATE_OFFER_DATA_FILE
from e2e_tests.utils.utils import log_the_result


def find_the_best_offer(page):
    results_page = ResultsPage(page)
    results = results_page.extract_result_data()
    return results_page.get_cheapest_high_rated(results)

def parse_and_log_the_data_to_file(offer):
    url_element = offer.locator('[itemprop="url"]')
    raw_url = url_element.get_attribute('content')
    rate_and_reviews = offer.locator("span", has_text="out of 5").first.text_content().split()
    offer_data = {
        'url': raw_url,
        'item_name': offer.locator("[data-testid='listing-card-name']").text_content(),
        'price_total':  offer.locator("span", has_text=" total").first.text_content().split()[0].replace("₪", ""),
        "rate": rate_and_reviews[0],
        "reviews": rate_and_reviews[6]
    }
    log_the_result(offer_data, OFFER_DETAILS_FILE)
    return offer_data

def validate_the_offer_match_json_data(page, offer, offer_parsed_data, logger):
    reservation = ReservationPage(page)
    reservation.click_on_offer(offer)
    for key, value in offer_parsed_data.items():
        if key == 'url':
            continue
        locator = page.locator(f"text={value}").first
        if locator.count() == 0:
            logger.info(f"Validation failed: '{value}' not visible for key '{key}'")
            return False
    return True

def parse_and_log_final_data_of_offer(page):
    reservation = ReservationPage(page)
    fee = reservation.get_final_fee_text()
    total = reservation.get_final_total_text()
    acc = reservation.get_final_accommodation_text()
    log_the_result({'fee': fee, 'total': total, 'accommodation': acc}, VALIDATE_OFFER_DATA_FILE)


def perform_search(page, check_in, check_out):
    search = SearchPage(page)
    search.enter_location(LOCATION)
    search.set_dates_for_travel(check_in, check_out)
    search.select_guests()
    search.submit_search()

def analyze_results(page):
    results_page = ResultsPage(page)
    page.wait_for_timeout(5000)
    results = results_page.extract_result_data()
    best_option = results_page.get_cheapest_high_rated(results)
    assert best_option, "No suitable result found"
    log_the_result(best_option, "selected_apartment.json")
    return best_option

def reserve_apartment(page):
    reservation = ReservationPage(page)
    reservation.attempt_reservation(PHONE_NUMBER)
    log_the_result({"phone": PHONE_NUMBER}, "reservation.json")