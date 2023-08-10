from Selenium.constants.api_path_constants import POST_SIGN_IN_USER, DELETE_USER
from Selenium.constants.user_credentials import USER_LOGIN_MAIN_USER, DEFAULT_PASSWORD
from Selenium.tests.test_base import TestBase
from Selenium.constants.url_constants import DEFAULT_API_URL


class TestRegistrationTest(TestBase):
    def setup_class(self):
        super().setup_class(self)
        self.user_email = USER_LOGIN_MAIN_USER
        self.user_password = DEFAULT_PASSWORD
        self.user_to_delete = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def test_registration_success_test(self):
        self.registration_facade.registration_full_cycle()
        assert len(self.garage_facade.get_text_from_empty_garage()) > 0

    def teardown_method(self):
        self.session.post(url=f"{DEFAULT_API_URL}{POST_SIGN_IN_USER}", json=self.user_to_delete)
        self.session.delete(f"{DEFAULT_API_URL}{DELETE_USER}")





