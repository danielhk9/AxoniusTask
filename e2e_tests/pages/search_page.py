# pages/search_page.py

from .base_page import BasePage
from ..constants.selectors import LOCATION_FIELD, GUESTS_BUTTON, INCREASE_BUTTON_ADULTS, INCREASE_BUTTON_CHILDREN


class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.location_input = f'[data-testid={LOCATION_FIELD}]'
        self.guests_button = f'[data-testid={GUESTS_BUTTON}]'
        self.adults_plus = f'[data-testid={INCREASE_BUTTON_ADULTS}]'
        self.children_plus = f'[data-testid={INCREASE_BUTTON_CHILDREN}]'
        self.search_button = f'[data-testid={GUESTS_BUTTON}]'

    def enter_location(self, location):
        self.fill(self.location_input, location)
        self.press_enter(self.location_input)

    def select_guests(self, adults=2, children=1):
        self.click(self.guests_button)
        for _ in range(adults):
            self.click(self.adults_plus)
        for _ in range(children):
            self.click(self.children_plus)

    def submit_search(self):
        self.click(self.search_button)

    def set_dates_for_travel(self, check_in, check_out):
        for date in [check_in, check_out]:
            self.page.locator(f"[data-state--date-string='{date}']").first.click()