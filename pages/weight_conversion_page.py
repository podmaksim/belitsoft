from pages.main_page import MainPage
from locators.weight_conversion_page_locator import WeightConversionPageLocator


class WeightConversionPage(MainPage):

    def conversion_ounces_to_grams(self):
        ounces_to_grams_button = self.find_element(
            WeightConversionPageLocator.LOCATOR_OUNCES_TO_GRAMS_BUTTON)
        ounces_to_grams_button.click()
