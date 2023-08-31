from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
from pages import AutodeclinePage, CreditScore


class EntityTypePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__title = (By.XPATH, ".//*[contains(text(),'Please, select your company type')]")
        self.__support = (By.XPATH, ".//*[contains(text(),'Support & Help')]")
        self.__answers = (By.XPATH, ".//li[@class = 'answer']")
        self.__answer_i_dont_have = (By.XPATH, ".//li[contains(text(), 'I don’t own a business yet')]")

    def check_go_to_first_question_of_quiz(self):
        time.sleep(1)
        first_question_title = self.driver.find_element(*self.__title)
        support = self.driver.find_element(*self.__support)
        if first_question_title.is_displayed() and support.is_displayed():
            return True

    def check_number_of_unactive_answers(self):
        number_of_answers: int = 5
        try:
            list_of_unactive_answer = self.driver.find_elements(*self.__answers)
            if len(list_of_unactive_answer) == number_of_answers:
                return True
        except Exception as unknown_exception:
            print(unknown_exception)
            return False

    def chose_answer_i_dont_own_business_yet(self):
        time.sleep(2)
        answer = self.driver.find_element(*self.__answer_i_dont_have)
        answer.click()
        return CreditScore

