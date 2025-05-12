from e2e_tests.conftest import find_the_best_offer, parse_and_log_the_data_to_file, log_the_result, \
    validate_the_offer_match_json_data, parse_and_log_final_data_of_offer
from e2e_tests.constants.selectors import INCREASE_BUTTON_ADULTS, INCREASE_BUTTON_CHILDREN
from e2e_tests.pages.conftest import set_location, set_dates_for_travel, \
    set_number_of_visitors, reserve_offer
from e2e_tests.pages.landing_page import click_on_search_button
from e2e_tests.constants.test_data import LOCATION, NUMBER_OF_ADULTS, NUMBER_OF_CHILDREN


def test_search_for_2_adults(home_page, get_random_dates, after_test, logger):
    logger.info("Starting searching for vacation")
    set_location(home_page, LOCATION)
    set_dates_for_travel(home_page, get_random_dates[0], get_random_dates[1])
    set_number_of_visitors(home_page, NUMBER_OF_ADULTS, INCREASE_BUTTON_ADULTS)
    set_number_of_visitors(home_page, NUMBER_OF_CHILDREN, INCREASE_BUTTON_CHILDREN, False)
    click_on_search_button(home_page)
    best_offer = find_the_best_offer(home_page)
    offer_parsed_data = parse_and_log_the_data_to_file(best_offer)
    verify_data = validate_the_offer_match_json_data(home_page, best_offer, offer_parsed_data, logger)
    expected_str = "\n".join([f"{k}: {v}" for k, v in offer_parsed_data.items()])
    assert verify_data is True, (
        f"The data does not match the JSON file.\n"
        f"Mismatch details, item url: {offer_parsed_data['url']}\n"
        f"Expected:\n{expected_str}"
    )
    reserve_offer(home_page, logger)
    parse_and_log_final_data_of_offer(home_page)




