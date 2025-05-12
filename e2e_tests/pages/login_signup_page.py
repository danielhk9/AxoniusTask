from e2e_tests.pages.base_page import wait_for_element_with_data_test_id


def _get_phone_number_field(page):
    return wait_for_element_with_data_test_id(page,  "login-signup-phonenumber")

def set_phone_number(page, phone_number):
    el = _get_phone_number_field(page)
    if el:
        el.type(phone_number)
    else:
        return 'there is no phone number field'