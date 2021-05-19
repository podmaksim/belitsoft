from pages.main_page import MainPage
from pages.weight_conversion_page import WeightConversionPage
from pages.ounces_to_grams_page import OunceToGramsPage


def test_change_user(browser, parameter_change):
    temperature, weight, length = parameter_change
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.choice_weight_button()
    weight_page = WeightConversionPage(browser)
    weight_page.conversion_ounces_to_grams()
    ounce_to_grams_page = OunceToGramsPage(browser)
    ounce_to_grams_page.enter_the_weight(weight)
    ounce_to_grams_page.print_result()
