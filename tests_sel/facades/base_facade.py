from ...tests_sel.pages.garage_page import GaragePage
from ...tests_sel.pages.navigation_bar_page import NavigationBarPage
from ...tests_sel.pages.registration_page import RegistrationPage
from ...tests_sel.pages.sign_in_page import SignInPage


class BaseFacade:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.navigation_bar_page = NavigationBarPage()
        self.sign_in_page = SignInPage()
        self.garage_page = GaragePage()