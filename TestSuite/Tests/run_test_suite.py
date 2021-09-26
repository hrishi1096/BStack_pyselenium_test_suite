# To run from the terminal
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.main_page import MainPage
from test_params import TestParams as params


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(params.WEBDRIVER_IMPLICIT_WAIT_TIME)
        self.driver.maximize_window()

    def test_001_founder_check(self):
        driver = self.driver
        driver.get(params.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_about_us_link()
        self.assertTrue(main_page.check_founders(params.BROWSERSTACK_FOUNDERS), "Founder check test failed")

    def test_002_login_valid(self):
        driver = self.driver
        driver.get(params.LOGIN_PAGE_URL)

        # Log in
        login = LoginPage(driver)
        login.enter_email_id(params.EMAIL_ID)
        login.enter_password(params.PASSWORD)
        login.click_sign_me_in()

        # Logout
        homepage = HomePage(driver)
        homepage.click_account_menu()
        homepage.click_logout()

    def test_003_login_invalid(self):
        driver = self.driver
        driver.get(params.LOGIN_PAGE_URL)
        login = LoginPage(driver)
        # Entering wrong username
        login.enter_email_id("12345678")
        # Clicking sign in without entering password
        login.click_sign_me_in()
        message = login.check_invalid_username_message()
        self.assertEqual(message, params.INVALID_EMAIL_MESSAGE)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()






