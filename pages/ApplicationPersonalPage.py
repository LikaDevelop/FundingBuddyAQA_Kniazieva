from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class ApplicationPersonalPage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__title = (By.XPATH, ".//h1[contains(text(), 'Applicant Info')]")

    def check_is_redirect(self):
        time.sleep(1)
        title = self.driver.find_element(*self.__title)
        if title.is_displayed():
            return True