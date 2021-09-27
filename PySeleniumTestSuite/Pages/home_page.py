from Locators.locators import Locators

class HomePage():
    def __init__(self, driver):
        self.driver = driver
        self.account_menu = Locators.account_menu_xpath
        self.logout_link = Locators.logout_link_xpath

    def click_account_menu(self):
        self.driver.find_element_by_xpath(self.account_menu).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link).click()

