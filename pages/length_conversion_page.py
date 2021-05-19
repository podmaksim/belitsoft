from pages.main_page import MainPage
from locators.length_conversion_page_locator import LengthConversionPageLocator


class LengthConversionPage(MainPage):

    def conversion_meters_to_feet(self):
        meters_to_feet_button = self.find_element(
            LengthConversionPageLocator.LOCATOR_METERS_TO_FEET_BUTTON)
        meters_to_feet_button.click()
