from selenium.webdriver.common.by import By


class MainPageLocator:
    LOCATOR_TEMPERATURE_BUTTON = (By.XPATH, '//div[@id="typeMenu"]//a[@class="typeConv temperature bluebg"]')
    LOCATOR_WEIGHT_BUTTON = (By.XPATH, '//div[@id="typeMenu"]//a[@class="typeConv weight bluebg"]')
    LOCATOR_LENGTH_BUTTON = (By.XPATH, '//div[@id="typeMenu"]//a[@class="typeConv length bluebg"]')
