from pages.temperature_conversion_page import TemperatureConversionPage
from locators.celsius_to_fahrenheit_page_locator import CelsiusToFahrenheitPageLocator


class CelsiusToFahrenheitPage(TemperatureConversionPage):

    def enter_the_temperature(self, temperature):
        enter_field = self.find_element(
            CelsiusToFahrenheitPageLocator.LOCATOR_ENTER_FIELD)
        enter_field.send_keys(temperature)

    def print_result(self):
        result = self.find_element(
            CelsiusToFahrenheitPageLocator.LOCATOR_ANSWER)
        print(result.text)
