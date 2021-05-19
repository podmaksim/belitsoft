from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocator


class MainPage(BasePage):

    def choice_temperature_button(self):
        temperature_button = self.find_element(
            MainPageLocator.LOCATOR_TEMPERATURE_BUTTON)
        temperature_button.click()

    def choice_weight_button(self):
        weight_button = self.find_element(
            MainPageLocator.LOCATOR_WEIGHT_BUTTON)
        weight_button.click()

    def choice_length_button(self):
        length_button = self.find_element(
            MainPageLocator.LOCATOR_LENGTH_BUTTON)
        length_button.click()
