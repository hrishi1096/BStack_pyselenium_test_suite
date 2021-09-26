# To run from the terminal
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import unittest
from threading import Thread
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.main_page import MainPage
from Config.test_params import TestParams as tp
from Config.test_params import BstackCredentials as bstack
from parameterizing import ParameterizedTestCase
from capabilities import Capabilities



class BstackTests(ParameterizedTestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor='https://' + bstack.username + ':' + bstack.accessKey + '@hub-cloud.browserstack.com/wd/hub',
            desired_capabilities=self.param)
        self.driver.implicitly_wait(tp.WEBDRIVER_IMPLICIT_WAIT_TIME)
        self.driver.maximize_window()

    def test_001_founder_check(self):
        driver = self.driver
        driver.get(tp.MAIN_PAGE_URL)
        main_page = MainPage(driver)
        main_page.click_about_us_link()
        if main_page.check_founders(tp.BROWSERSTACK_FOUNDERS):
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                {"status":"passed", "reason": "Founder check passed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                {"status":"failed", "reason": "Founder check failed"}}')

    def test_002_login_valid(self):
        driver = self.driver
        driver.get(tp.LOGIN_PAGE_URL)

        # Log in
        login = LoginPage(driver)
        login.enter_email_id(tp.EMAIL_ID)
        login.enter_password(tp.PASSWORD)
        login.click_sign_me_in()

        # Logout
        homepage = HomePage(driver)
        homepage.click_account_menu()
        homepage.click_logout()

        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"passed", "reason": "Login valid passed!"}}')

    def test_003_login_invalid(self):
        driver = self.driver
        driver.get(tp.LOGIN_PAGE_URL)
        login = LoginPage(driver)
        # Entering wrong username
        login.enter_email_id("12345678")
        # Clicking sign in without entering password
        login.click_sign_me_in()
        message = login.check_invalid_username_message()
        if message == tp.INVALID_EMAIL_MESSAGE:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                {"status":"passed", "reason": "Login invalid passed!"}}')
        else:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": \
                {"status":"passed", "reason": "Login invalid failed!"}}')

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    for cap in Capabilities.caps:
        suite.addTest(ParameterizedTestCase.parameterize(BstackTests, param=cap))

    for cap in Capabilities.caps:
        Thread(target=unittest.TextTestRunner().run, args=(suite,)).start()








