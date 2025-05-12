import time

from e2e_tests.pages.base_page import wait_for_element_with_data_test_id, wait_for_element


def _get_the_search_button(page):
    return wait_for_element_with_data_test_id(page, 'structured-search-input-search-button')

def click_on_search_button(page):
    _get_the_search_button(page).click()

def _get_guests_button(page):
    return wait_for_element_with_data_test_id(page, 'structured-search-input-field-guests-button')

def click_on_guests_button(page):
    _get_guests_button(page).click()


def _get_the_increase_button(page, element):
    return wait_for_element_with_data_test_id(page, element)

def click_on_increase(page, element):
    _get_the_increase_button(page, element).click()


def _get_the_location_field(page):
    return wait_for_element_with_data_test_id(page, 'structured-search-input-field-query')

def type_inside_location_field(page, location):
    el = _get_the_location_field(page)
    el.click()
    el.type(location)

def _get_check_in_button(page):
    return wait_for_element_with_data_test_id(page, 'structured-search-input-field-split-dates-0')

def click_on_check_in_button(page):
    _get_check_in_button(page).click()

def select_specific_date(page,date):
    page.click(f"[data-state--date-string='{date}']")

def wait_for_search_results(page):
    return wait_for_element_with_data_test_id(page, 'stays-page-heading')

def get_all_offers(page, retries=3, delay=5):
    selector = 'div[itemprop="itemListElement"][itemtype="http://schema.org/ListItem"]'
    for _ in range(retries):
        try:
            el = wait_for_element(page, selector)
            if el.count() > 1:
                return el
        except TimeoutError:
            pass
        time.sleep(delay)
    return None

#if locator.count() > 1:
