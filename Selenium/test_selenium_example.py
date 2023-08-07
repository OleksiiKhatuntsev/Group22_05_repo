from selenium.webdriver.common.by import By
import requests

from registration_page import RegistrationPage
from custom_driver import Driver


class TestRegistrationTest:
    def setup_class(self):
        self.driver = Driver().driver
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

        self.registration_page = RegistrationPage()
        self.session = requests.session()
        self.user_email = "tesdfjasdhssasdadkhfkjsdfsdfls@jfkfla.kjd"
        self.user_password = "Qwerty123"

    def test_registration_success_test(self):
        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        sign_in_button.click()
        self.driver.find_element(By.XPATH, "//button[text()='Registration']").click()
        self.registration_page.name_field().send_keys("TestName")
        self.registration_page.last_name_field().send_keys("TestLastName")
        self.registration_page.email_field().send_keys(self.user_email)
        self.registration_page.password_field().send_keys(self.user_password)
        self.registration_page.reenter_password_field().send_keys(self.user_password)
        self.registration_page.register_button().click()
        assert len(self.driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")) > 0


    def teardown_method(self):
        user_to_delete = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_to_delete)
        self.session.delete("https://qauto2.forstudy.space/api/users")





