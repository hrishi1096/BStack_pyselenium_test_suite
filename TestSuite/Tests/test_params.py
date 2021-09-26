import os


class TestParams():
    WEBDRIVER_IMPLICIT_WAIT_TIME = 10
    BROWSERSTACK_FOUNDERS = ["Ritesh Arora", "Nakul Aggarwal"]
    MAIN_PAGE_URL = "https://www.browserstack.com"
    LOGIN_PAGE_URL = "https://www.browserstack.com/users/sign_in"
    EMAIL_ID = "test_account96@yahoo.com"
    PASSWORD = "TestAccountBstack@123"
    INVALID_EMAIL_MESSAGE = "Invalid Email"

class BstackCredentials():
    username = os.environ['BROWSERSTACK_USERNAME'];
    accessKey = os.environ['BROWSERSTACK_ACCESS_KEY'];