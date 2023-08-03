from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.chrome.options import Options

class TestRegistrationTest:
    def setup_class(self):
        chop = webdriver.ChromeOptions()

        chop.add_extension("C:\\Users\\Kaelthas\\Downloads\\Google-Translate.crx")

        # create new Chrome driver object with Chrome extension

        driver = webdriver.Chrome(chop)
        driver.get("https://google.com")
        options = Options()
        options.add_argument("--headless")

        self.driver = webdriver.Chrome(options)
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.driver.implicitly_wait(5)
        # self.driver.set_window_size(200, 200)

        self.session = requests.session()
        self.user_email = "tesdfjasdhssasdadkhfkjsdfsdfls@jfkfla.kjd"
        self.user_password = "Qwerty123"

    def test_registration_success_test(self):
        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        sign_in_button.click()
        self.driver.find_element(By.XPATH, "//button[text()='Registration']").click()
        name_field = self.driver.find_element(By.ID, "signupName")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        reenter_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")
        name_field.send_keys("TestName")
        last_name_field.send_keys("TestLastName")
        email_field.send_keys(self.user_email)
        password_field.send_keys(self.user_password)
        reenter_password_field.send_keys(self.user_password)
        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
        assert len(self.driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")) > 0


    def teardown_method(self):
        user_to_delete = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_to_delete)
        self.session.delete("https://qauto2.forstudy.space/api/users")





