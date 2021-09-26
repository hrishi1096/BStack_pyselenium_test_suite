from Locators.locators import Locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class MainPage():
    def __init__(self, driver):
        self.driver = driver
        self.about_us_link = Locators.about_us_xpath

    def click_about_us_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.about_us_link)))
        self.driver.find_element_by_xpath(self.about_us_link).click()

    def check_founders(self, founders):
        for founder in founders:
            try:
                self.driver.find_element_by_link_text(founder)
            except NoSuchElementException:
                return False

        return True
