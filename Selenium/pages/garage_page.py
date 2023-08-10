from selenium.webdriver.common.by import By
from .base_page import BasePage
from ..controls.label import Label


class GaragePage(BasePage):
    def __init__(self):
        super().__init__()
        self.empty_garage_label = lambda: Label(self._driver.find_element(By.XPATH, "//p[text()='You don’t have any cars in your garage']"))