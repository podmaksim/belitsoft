from pages.main_page import MainPage
from locators.temperature_conversion_page_locator import TemperatureConversionPageLocator


class TemperatureConversionPage(MainPage):

    def conversion_celsius_to_fahrenheit(self):
        celsius_to_fahrenheit_button = self.find_element(
            TemperatureConversionPageLocator.LOCATOR_CELSIUS_FAHRENHEIT_BUTTON)
        celsius_to_fahrenheit_button.click()
