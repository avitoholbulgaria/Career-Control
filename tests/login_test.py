import time
import unittest

from selenium import webdriver

from pom.login_page import LoginPage
from test_data import TestData


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(TestData.CHROME_DRIVER_LOCATION)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_login_with_valid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(TestData.VALID_USERNAME)
        login_page.enter_password(TestData.VALID_PASSWORD)

        login_page.click_login_button()
        time.sleep(2)
        assert self.driver.title == TestData.COMPANY_NAME

    def test_login_with_invalid_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(TestData.INVALID_USERNAME)
        login_page.enter_password(TestData.VALID_PASSWORD)

        login_page.click_login_button()

        assert login_page.get_error_message() == TestData.LOGIN_ERROR_MESSAGE

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
