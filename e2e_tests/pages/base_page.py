class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def press_enter(self, locator):
        self.page.locator(locator).press("Enter")

    def wait_for_selector(self, locator, timeout=5000):
        self.page.locator(locator).wait_for(timeout=timeout)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def get_elements(self, locator):
        return self.page.locator(locator).all()
