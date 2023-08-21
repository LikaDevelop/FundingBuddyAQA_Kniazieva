from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class OfferPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__my_account = (By.XPATH, ".//a[@class = 'account font-14']")
        self.__log_out = (By.XPATH, ".//button [@class='log-out-btn font-14']")

    def check_log_in(self):
        time.sleep(1)
        my_account = self.driver.find_element(*self.__my_account)
        log_out = self.driver.find_element(*self.__log_out)
        if my_account.is_displayed() and log_out.is_displayed():
            return True

