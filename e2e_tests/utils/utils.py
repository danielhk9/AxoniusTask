import os
import json
import logging

from e2e_tests.constants.test_data import TIMEOUT

logger = logging.getLogger(__name__)

def log_the_result(offer_data, file_name):
    os.makedirs("temp", exist_ok=True)
    with open(f"temp/{file_name}.json", "w", encoding="utf-8") as f:
        json.dump(offer_data, f, indent=4)
    logger.info(f"Saved data to temp/{file_name}.json")

def wait_for_element(page, selector, timeout=TIMEOUT, last=False):
    try:
        locator = page.locator(selector)
        locator.first.wait_for(state="attached", timeout=timeout)
        return locator.last if last else locator
    except TimeoutError:
        logger.error(f'Selector element {selector} was not found')
        return False
