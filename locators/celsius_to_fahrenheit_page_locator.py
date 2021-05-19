from selenium.webdriver.common.by import By


class CelsiusToFahrenheitPageLocator:
    LOCATOR_ENTER_FIELD = (By.ID, 'argumentConv')
    LOCATOR_ANSWER = (By.ID, 'answer')
