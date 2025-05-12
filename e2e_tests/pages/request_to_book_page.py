from e2e_tests.constants.selectors import TOTAL, ACCOMMODATION, CLEANING_FEE, AIRBNB_GUEST_FEE, PHONE_NUMBER_EL
from e2e_tests.pages.base_page import wait_for_element_with_data_test_id

def _get_phone_number_field(page):
    return wait_for_element_with_data_test_id(page,  PHONE_NUMBER_EL)

def set_phone_number(page, phone_number, logger):
    el = _get_phone_number_field(page)
    if el:
        logger.info("Found phone number field. Typing phone number...")
        el.type(phone_number)
    else:
        logger.warning('there is no phone number field')


def get_final_total_text(page):
    return wait_for_element_with_data_test_id(page, TOTAL).text_content()

def get_final_accommodation_text(page):
    return wait_for_element_with_data_test_id(page, ACCOMMODATION).text_content()

def get_final_fee_text(page):
    for fee_type in [CLEANING_FEE, AIRBNB_GUEST_FEE]:
        el = wait_for_element_with_data_test_id(page, fee_type)
        if el:
            return el.text_content()
    return "There is no FEE tax"
