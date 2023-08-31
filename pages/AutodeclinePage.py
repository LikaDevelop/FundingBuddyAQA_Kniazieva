from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

class AutodeclinePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__title = (By.XPATH, ".//h1[contains(text(), 'Unfortunatly, we are currently only able to help established')]")
        self.__btn_back = (By.XPATH, ".//button[@class = 'nav-button-icon nav-button-icon-left d-flex']")

    def check_go_to_autodecline(self):
        time.sleep(1)
        autodecline_title = self.driver.find_element(*self.__title)
        btn_back = self.driver.find_element(*self.__btn_back)
        if autodecline_title.is_displayed() and btn_back.is_displayed():
            return True

