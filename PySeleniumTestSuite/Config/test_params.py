import os

# All the parameters to be used by the tests and the Browserstack username
# and access key

class TestParams():
    WEBDRIVER_IMPLICIT_WAIT_TIME = 10
    BROWSERSTACK_FOUNDERS = ["Ritesh Arora", "Nakul Aggarwal"]
    MAIN_PAGE_URL = "https://www.browserstack.com"
    LOGIN_PAGE_URL = "https://www.browserstack.com/users/sign_in"
    POST_LOGOUT_URL = "https://www.browserstack.com/live"
    EMAIL_ID = "test_account96@yahoo.com"
    PASSWORD = "TestAccountBstack@123"
    INVALID_EMAIL_MESSAGE = "Invalid Email"


class BstackCredentials():
    username = os.environ['BROWSERSTACK_USERNAME']
    accessKey = os.environ['BROWSERSTACK_ACCESS_KEY']