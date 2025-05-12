import logging
from playwright.sync_api import TimeoutError
from e2e_tests.constants.test_data import TIMEOUT
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def wait_for_element_with_data_test_id(page, selector, timeout=TIMEOUT):
    try:
        element = page.locator(f"[data-testid='{selector}']")
        element.wait_for(state="attached", timeout=timeout)
        return element
    except TimeoutError:
        logger.error(f'Selector element {selector} was not found')
        return False


def wait_for_element(page, selector, timeout=TIMEOUT, last=False):
    try:
        locator = page.locator(selector)
        locator.first.wait_for(state="attached", timeout=timeout)
        if last:
            return locator.last
        return locator
    except TimeoutError:
        logger.error(f'Selector element {selector} was not found')
        return False