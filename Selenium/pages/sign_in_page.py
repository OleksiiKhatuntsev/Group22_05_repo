from selenium.webdriver.common.by import By
from Selenium.controls.button import Button
from .base_page import BasePage


class SignInPage(BasePage):
    def __init__(self):
        super().__init__()
        self.register_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Registration']"))