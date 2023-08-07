from selenium.webdriver.common.by import By

from text_box import TextBox
from button import Button
from base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self):
        super().__init__()
        self.name_field = lambda: TextBox(self._driver.find_element(By.ID, "signupName"))
        self.last_name_field = lambda: TextBox(self._driver.find_element(By.ID, "signupLastName"))
        self.email_field = lambda: TextBox(self._driver.find_element(By.ID, "signupEmail"))
        self.password_field = lambda: TextBox(self._driver.find_element(By.ID, "signupPassword"))
        self.reenter_password_field = lambda: TextBox(self._driver.find_element(By.ID, "signupRepeatPassword"))
        self.register_button = lambda: Button(self._driver.find_element(By.XPATH, "//button[text()='Register']"))
