# pages/reservation_page.py

from .base_page import BasePage
from ..constants.selectors import RESERVE_BUTTON_XPATH, CONTINUE_BUTTON_XPATH, TRANSLATION_MODAL_TITLE_XPATH, \
    FINAL_FEE_SELECTOR, FINAL_TOTAL_SELECTOR, FINAL_ACCOMMODATION_SELECTOR, PHONE_NUMBER_EL
from ..utils.utils import wait_for_element


class ReservationPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_on_offer(self, offer_element):
        offer_element.click()

    def click_reserve(self):
        wait_for_element(self.page, RESERVE_BUTTON_XPATH, last=True).click()

    def click_continue(self):
        wait_for_element(self.page, CONTINUE_BUTTON_XPATH).click()

    def close_translate_popup_if_exists(self):
        try:
            if wait_for_element(self.page, TRANSLATION_MODAL_TITLE_XPATH, timeout=2000):
                self.page.keyboard.press("Escape")
        except:
            pass

    def get_final_fee_text(self):
        return self.page.locator(FINAL_FEE_SELECTOR).inner_text()

    def get_final_total_text(self):
        return self.page.locator(FINAL_TOTAL_SELECTOR).inner_text()

    def attempt_reservation(self, phone_number):
        self.click_reserve()
        wait_for_element(self.page, PHONE_NUMBER_EL).fill(phone_number)

    def confirm_details(self):
        wait_for_element(self.page, CONFIRM_BUTTON_SELECTOR).click()

    def get_final_accommodation_text(self):
        return self.page.locator(FINAL_ACCOMMODATION_SELECTOR).inner_text()
