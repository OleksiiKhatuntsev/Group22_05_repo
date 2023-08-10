from Selenium.pages.garage_page import GaragePage
from Selenium.pages.navigation_bar_page import NavigationBarPage
from Selenium.pages.registration_page import RegistrationPage
from Selenium.pages.sign_in_page import SignInPage


class BaseFacade:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.navigation_bar_page = NavigationBarPage()
        self.sign_in_page = SignInPage()
        self.garage_page = GaragePage()