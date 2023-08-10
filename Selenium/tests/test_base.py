import requests

from Selenium.driver.custom_driver import Driver
from Selenium.facades.garage_facade import GarageFacade
from Selenium.facades.registration_facade import RegistrationFacade
from Selenium.pages.registration_page import RegistrationPage
from Selenium.constants.url_constants import DEFAULT_URL


class TestBase:
    def setup_class(self):
        self.driver = Driver().driver
        self.driver.get(DEFAULT_URL)
        self.registration_facade = RegistrationFacade()
        self.garage_facade = GarageFacade()
        self.session = requests.session()