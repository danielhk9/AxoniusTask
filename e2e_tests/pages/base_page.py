from playwright.sync_api import TimeoutError

def wait_for_element_with_data_test_id(page, selector, timeout=5000):  # timeout in ms
    try:
        element = page.locator(f"[data-testid='{selector}']")
        element.wait_for(state="attached", timeout=timeout)
        return element
    except TimeoutError:
        return False


def wait_for_element(page, selector, timeout=10000, last=False):
    try:
        locator = page.locator(selector)
        locator.first.wait_for(state="attached", timeout=timeout)
        if last:
            return locator.last
        return locator
    except TimeoutError:
        return None