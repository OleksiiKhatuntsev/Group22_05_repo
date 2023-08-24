# import sys
# sys.path.append("..")
import time
from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from pytest_contexts import Context
from ...tests_sel.driver.custom_driver import Driver

from ...tests_sel.constants.api_path_constants import DELETE_USER, POST_SIGN_IN_USER
from ...tests_sel.constants.url_constants import DEFAULT_API_URL
from ...tests_sel.constants.user_credentials import USER_LOGIN_MAIN_USER, DEFAULT_PASSWORD
# from constants.api_path_constants import DELETE_USER, POST_SIGN_IN_USER
# from constants.url_constants import DEFAULT_API_URL
# from constants.user_credentials import USER_LOGIN_MAIN_USER, DEFAULT_PASSWORD
from ...tests_sel.tests.test_base import TestBase


def decorator_screenshot(func):
    driver = Driver().driver
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except AssertionError:
            allure.attach(driver.get_screenshot_as_png(), name="FAILED SCREEN",
                          attachment_type=AttachmentType.PNG)
            raise

    return wrapper

@allure.suite("RegistrationTests")
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




    @allure.link("TestRailLink", "https://google.com")
    @allure.issue("JiraLink", "https://google.com")
    @allure.feature("Stable")
    @decorator_screenshot
    def test_registration_success_test(self):
        assert False
        # assert False

        self.registration_facade.registration_full_cycle()
        allure.attach(self.driver.get_screenshot_as_png(), name="Before registraion",
                      attachment_type=AttachmentType.PNG)
        assert len(self.garage_facade.get_text_from_empty_garage()) > 0

    # make a screenshot with a name of the test, date and time

    def test_new_test(self):
        assert False


    def test_new_test_2(self):
        a = 2/0

    def teardown_method(self):
        self.session.post(url=f"{DEFAULT_API_URL}{POST_SIGN_IN_USER}", json=self.user_to_delete)
        self.session.delete(f"{DEFAULT_API_URL}{DELETE_USER}")