from datetime import date, timedelta
import random
import pytest
from playwright.sync_api import Browser


from e2e_tests.config import BASE_URL


@pytest.fixture(scope="session")
def home_page(browser: Browser):
    page = browser.new_page()
    page.goto(BASE_URL)
    yield page
    page.close()

@pytest.fixture(scope="function")
def after_test(home_page):
    yield
    home_page.goto(BASE_URL)

@pytest.fixture(scope="function")
def get_random_dates():
    today = date.today()
    check_in_offset = random.randint(0, 28)
    check_out_offset = check_in_offset + random.randint(1, 5)
    check_in = today + timedelta(days=check_in_offset)
    check_out = today + timedelta(days=check_out_offset)
    return check_in.strftime('%Y-%m-%d'), check_out.strftime('%Y-%m-%d')

@pytest.fixture(scope="function")
def logger():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    return logging.getLogger(__name__)
