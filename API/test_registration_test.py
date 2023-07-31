import requests
import json


class UserLoginModel:
    def __init__(self, email: str, password: str, remember: bool):
        self.email = email
        self.password = password
        self.remember = remember

class UserEmailPasswordModel:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password

class TestLoginTest:

    def setup_class(self):

        with open("test_data.json") as config:
            lines = json.loads(config.read())
        self.user = UserEmailPasswordModel(lines["test_user_1_email"], lines["test_user_1_password"])
        self.session = requests.session()

        print("\n START")

    def test_registration_success(self):
        success_registration_test_data = {
            "name": "John",
            "lastName": "Dou",
            "email": self.user.email,
            "password": self.user.password,
            "repeatPassword": self.user.password
        }
        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signup', json=success_registration_test_data)
        assert result.json()["status"] == "ok"

    def test_registration_password_failed_check(self):
        success_registration_test_data = {
            "name": "John",
            "lastName": "Dou",
            "email": self.user.email,
            "password": self.user.password,
            "repeatPassword": 123
        }
        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signup', json=success_registration_test_data)
        assert result.json()["status"] == "error"



    def teardown_method(self):
        # login_dict = {"email": self.user_mail,
        # "password": self.user_password,
        # "remember": False}
        login_user = UserLoginModel(self.user.email, self.user.password, True)

        result = self.session.post(url='https://qauto2.forstudy.space/api/auth/signin', json=login_user.__dict__)
        self.session.delete(url="https://qauto2.forstudy.space/api/users/")