from e2e_tests.pages.base_page import wait_for_element


def click_on_offer(offer2):
    offer2.click()

def _get_reserve_button(page):
    return wait_for_element(page, '//span[text()="Reserve"]', last=True)

def click_on_reserve(page):
    _get_reserve_button(page).click()

def _get_on_continue_button(page):
    return wait_for_element(page, '//button[text()="Continue"]')

def click_on_continue_button(page):
    _get_on_continue_button(page).click()

def close_translate_window(page):
    if wait_for_element(page, '//h1[text()="Translation on"]'):
        page.keyboard.press("Escape")