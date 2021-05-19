from pages.main_page import MainPage
from pages.temperature_conversion_page import TemperatureConversionPage
from pages.celsius_to_fahrenheit_page import CelsiusToFahrenheitPage


def test_change_user(browser, parameter_change):
    temperature, weight, length = parameter_change
    main_page = MainPage(browser)
    main_page.open_base_page()
    main_page.choice_temperature_button()
    temperature_page = TemperatureConversionPage(browser)
    temperature_page.conversion_celsius_to_fahrenheit()
    celsius_page = CelsiusToFahrenheitPage(browser)
    celsius_page.enter_the_temperature(temperature)
    celsius_page.print_result()

