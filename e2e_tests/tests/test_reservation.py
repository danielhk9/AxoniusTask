
from e2e_tests.config import BASE_URL
from e2e_tests.utils.airbnb_actions import perform_search, analyze_results, reserve_apartment

def test_airbnb_flow(home_page, get_random_dates):
    check_in, check_out = get_random_dates
    home_page.goto(BASE_URL)
    perform_search(home_page, check_in, check_out)
    analyze_results(home_page)
    reserve_apartment(home_page)