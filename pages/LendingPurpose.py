from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages import RegistrationPage


class LendingPurpose:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__answer_advertising = (By.XPATH, ".//li[contains(text(), 'Advertising')]")

    def choose_answer_advertising(self):
        answer = self.driver.find_element(*self.__answer_advertising)
        answer.click()
        return RegistrationPage

