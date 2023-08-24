import requests

from ...tests_sel.driver.custom_driver import Driver
from ...tests_sel.facades.garage_facade import GarageFacade
from ...tests_sel.facades.registration_facade import RegistrationFacade
from ...tests_sel.pages.registration_page import RegistrationPage
from ...tests_sel.constants.url_constants import DEFAULT_URL


class TestBase:
    def setup_class(self):
        self.driver = Driver().driver
        self.driver.get(DEFAULT_URL)
        self.registration_facade = RegistrationFacade()
        self.garage_facade = GarageFacade()
        self.session = requests.session()