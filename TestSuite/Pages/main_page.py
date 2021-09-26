from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException

class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.about_us_link = Locators.about_us_xpath

    def click_about_us_link(self):
        self.driver.find_element_by_xpath(self.about_us_link).click()

    def check_founders(self, founders):
        for founder in founders:
            try:
                self.driver.find_element_by_link_text(founder)
            except NoSuchElementException:
                return False

        return True
