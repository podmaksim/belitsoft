from pages.length_conversion_page import LengthConversionPage
from locators.meters_to_feet_page_locator import MetersToFeetPageLocator


class MetersToFeetPage(LengthConversionPage):

    def enter_the_length(self, length):
        enter_field = self.find_element(
            MetersToFeetPageLocator.LOCATOR_ENTER_FIELD)
        enter_field.send_keys(length)

    def print_result(self):
        result = self.find_element(
            MetersToFeetPageLocator.LOCATOR_ANSWER)
        print(result.text)
