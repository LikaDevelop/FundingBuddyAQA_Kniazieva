import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages import LendingPurpose, CreditScore


class LendingAmount:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__answer_5000_10000 = (By.XPATH, ".//li[contains(text(), '$5,000 - $10,000')]")
        self.__btn_back = (By.XPATH, ".//button[@class = 'nav-button-icon nav-button-icon-left d-flex']")
        self.__title = (By.XPATH, ".//h1[contains(text(), 'How much capital do you need?')]")

    def choose_answer_5000_10000(self):
        answer = self.driver.find_element(*self.__answer_5000_10000)
        answer.click()
        return LendingPurpose

    def click_on_the_btn_back(self):
        button = self.driver.find_element(*self.__btn_back)
        button.click()
        return CreditScore

    def check_is_redirect(self):
        time.sleep(1)
        title = self.driver.find_element(*self.__title)
        if title.is_displayed():
            return True




