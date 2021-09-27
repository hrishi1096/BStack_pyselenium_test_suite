from Locators.locators import Locators

class LoginPage():
    def __init__(self, driver):
        self.driver = driver
        self.email_textbox  = Locators.email_textbox_xpath
        self.password_textbox    = Locators.password_textbox_xpath
        self.sign_me_in_button = Locators.sign_me_in_button_xpath
        self.invalid_username_message = Locators.invalid_username_message_xpath

    def enter_email_id(self, email_id):
        self.driver.find_element_by_xpath(self.email_textbox).clear()
        self.driver.find_element_by_xpath(self.email_textbox).send_keys(email_id)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).clear()
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    def click_sign_me_in(self):
        return self.driver.find_element_by_xpath(self.sign_me_in_button).click()

    def check_invalid_username_message(self):
        return self.driver.find_element_by_xpath(self.invalid_username_message).text




