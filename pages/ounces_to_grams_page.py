from pages.weight_conversion_page import WeightConversionPage
from locators.ounces_to_grams_page_locator import OuncesToGramsPageLocator


class OunceToGramsPage(WeightConversionPage):

    def enter_the_weight(self, weight):
        enter_field = self.find_element(
            OuncesToGramsPageLocator.LOCATOR_ENTER_FIELD)
        enter_field.send_keys(weight)

    def print_result(self):
        result = self.find_element(
            OuncesToGramsPageLocator.LOCATOR_ANSWER)
        print(result.text)
