# To run from the terminal
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


from threading import Thread
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.main_page import MainPage
from Config.test_params import TestParams as tp
from Config.test_params import BstackCredentials as bstack
from capabilities import Capabilities



def setup(desired_cap):
    driver = webdriver.Remote(
        command_executor='https://' + bstack.username + ':' + bstack.accessKey + '@hub-cloud.browserstack.com/wd/hub',
        desired_capabilities=desired_cap)
    driver.implicitly_wait(tp.WEBDRIVER_IMPLICIT_WAIT_TIME)
    driver.maximize_window()
    return driver



def founder_check_test(desired_cap):
    driver = setup(desired_cap)
    driver.get(tp.MAIN_PAGE_URL)

    main_page = MainPage(driver)
    main_page.click_about_us_link()
    if main_page.check_founders(tp.BROWSERSTACK_FOUNDERS):
        print("founder check passed")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"passed", "reason": "Founder check passed!"}}')
    else:
        print("founder check failed")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"failed", "reason": "Founder check failed"}}')
    driver.close()



def login_valid_test(desired_cap):
    driver = setup(desired_cap)
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

    if driver.current_url == tp.POST_LOGOUT_URL:
        print("login valid passed")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"passed", "reason": "Login valid test passed!"}}')
    else:
        print("login valid failed")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"failed", "reason": "Login valid test failed"}}')
    driver.close()



def login_invalid_test(desired_cap):
    driver = setup(desired_cap)
    driver.get(tp.LOGIN_PAGE_URL)
    login = LoginPage(driver)

    # Entering wrong username
    login.enter_email_id("12345678")

    # Clicking sign in without entering password
    login.click_sign_me_in()
    message = login.check_invalid_username_message()
    if message == tp.INVALID_EMAIL_MESSAGE:
        print("login invalid passed")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"passed", "reason": "Login invalid test passed!"}}')
    else:
        print("login invalid failed")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": \
            {"status":"passed", "reason": "Login invalid test failed!"}}')
    driver.close()



def run_test_suite(desired_cap):
    founder_check_test(desired_cap)
    login_valid_test(desired_cap)
    login_invalid_test(desired_cap)
    driver.quit()


if __name__ == "__main__":
    for cap in Capabilities.caps:
        Thread(target=run_test_suite, args=(cap,)).start()






