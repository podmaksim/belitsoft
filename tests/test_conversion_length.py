from pages.main_page import MainPage
from pages.length_conversion_page import LengthConversionPage
from pages.meters_to_feet_page import MetersToFeetPage


def test_change_user(browser, parameter_change):
    temperature, weight, length = parameter_change
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.choice_length_button()
    length_page = LengthConversionPage(browser)
    length_page.conversion_meters_to_feet()
    meters_to_feet_page = MetersToFeetPage(browser)
    meters_to_feet_page.enter_the_length(length)
    meters_to_feet_page.print_result()
