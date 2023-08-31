import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages import AutodeclinePage
from pages.LendingAmout import LendingAmount


class CreditScore:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__answer_below_500 = (By.XPATH, ".//li[contains(text(), 'Below 500')]")
        self.__answer_700 = (By.XPATH, ".//li[contains(text(), '700 +')]")
        self.__answer_651 = (By.XPATH, ".//li[contains(text(), '651 - 700')]")
        self.__select_answer_651 = (By.XPATH, ".//button[contains(text(), \"651 - 700\")]")
        self.__title = (By.XPATH, ".//h1[contains(text(), 'What is your approximate credit score?')]")
        self.__active_answer = (By.CSS_SELECTOR, "li.answer.active")

    def choose_answer_below_500(self):
        answer = self.driver.find_element(*self.__answer_below_500)
        answer.click()
        return AutodeclinePage

    def choose_answer_700(self):
        answer = self.driver.find_element(*self.__answer_700)
        answer.click()
        return LendingAmount

    def rechoose_answer_651(self):
        time.sleep(1)
        answer = self.driver.find_element(*self.__answer_651)
        answer.click()
        return self

    def select_answer_651(self):
        time.sleep(1)
        answer = self.driver.find_element(*self.__select_answer_651)
        answer.click()
        return LendingAmount


    def check_is_redirect_to_credit_score(self):
        time.sleep(1)
        title = self.driver.find_element(*self.__title)
        active_answer = self.driver.find_element(*self.__active_answer)
        if title.is_displayed() and active_answer.is_displayed():
            return True
