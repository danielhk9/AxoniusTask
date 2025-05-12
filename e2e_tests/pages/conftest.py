from e2e_tests.pages.item_page import click_on_reserve, click_on_continue_button, close_translate_window
from e2e_tests.pages.landing_page import click_on_guests_button, click_on_increase, type_inside_location_field, \
    click_on_check_in_button, select_specific_date
from e2e_tests.pages.login_signup_page import set_phone_number
from e2e_tests.test_data import PHONE_NUMBER


def _set_number_of_guests(page, number, element):
    for _ in range(number):
        click_on_increase(page, element)

def set_number_of_visitors(page, number, element, should_press_on_guests_button=True):
    if should_press_on_guests_button:
        click_on_guests_button(page)
    _set_number_of_guests(page, number, element)

def set_location(page, location):
    type_inside_location_field(page, location)

def set_dates_for_travel(page,check_in, check_out):
    click_on_check_in_button(page)
    for date in [check_in, check_out]:
        select_specific_date(page, date)

def navigate_to_offer(page, offer):
    url_element = offer.locator('[itemprop="url"]')
    raw_url = url_element.get_attribute('content')
    full_url = f"https://{raw_url}"
    page.goto(full_url, wait_until="load")
    close_translate_window(page)


def reserve_offer(page, offer):
    click_on_reserve(page)
    set_phone_number(page, PHONE_NUMBER)

def sign_up_to_website(page):
    click_on_continue_button(page)

