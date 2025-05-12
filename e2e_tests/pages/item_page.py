from e2e_tests.constants.selectors import RESERVE_BUTTON_XPATH, CONTINUE_BUTTON_XPATH, TRANSLATION_MODAL_TITLE_XPATH
from e2e_tests.pages.base_page import wait_for_element


def click_on_offer(offer2):
    offer2.click()

def _get_reserve_button(page):
    return wait_for_element(page, RESERVE_BUTTON_XPATH, last=True)

def click_on_reserve(page):
    _get_reserve_button(page).click()

def _get_on_continue_button(page):
    return wait_for_element(page, CONTINUE_BUTTON_XPATH)

def click_on_continue_button(page):
    _get_on_continue_button(page).click()

def close_translate_window_if_exists(page):
    if wait_for_element(page, TRANSLATION_MODAL_TITLE_XPATH):
        page.keyboard.press("Escape")