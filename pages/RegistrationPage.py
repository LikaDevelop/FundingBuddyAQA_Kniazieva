import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages import ApplicationPersonalPage


class RegistrationPage:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__registration_title = (By.XPATH, ".//h1[contains(text(), 'You are prequalified for alternative funding!')]")
        self.__btn_continue = (By.XPATH, ".//button[@class = 'nav-button-icon nav-button-icon-right d-flex']")
        self.__full_name = (By.XPATH, ".//input[@id = 'fullName']")
        self.__cell_phone = (By.XPATH, ".//input[@id = 'cellPhone']")
        self.__email = (By.XPATH, ".//input[@id = 'email']")
        self.__password = (By.XPATH, ".//input[@id = 'password']")


    def check_is_redirect_to_registration_form(self):
        time.sleep(1)
        registration_title = self.driver.find_element(*self.__registration_title)
        btn_continue = self.driver.find_element(*self.__btn_continue)
        if registration_title.is_displayed() and btn_continue.is_displayed():
            return True

    def fill_in_full_name(self, name: str):
        time.sleep(1)
        full_name = self.driver.find_element(*self.__full_name)
        full_name.send_keys(name)
        return self

    def full_in_cell_phone(self, cell_phone_text: str):
        time.sleep(1)
        cell_phone = self.driver.find_element(*self.__cell_phone)
        cell_phone.send_keys(cell_phone_text)
        return self

    def full_in_email(self, email_text: str):
        time.sleep(1)
        email = self.driver.find_element(*self.__email)
        email.send_keys(email_text)
        return self

    def full_in_password(self, password_text: str):
        time.sleep(1)
        password = self.driver.find_element(*self.__password)
        password.send_keys(password_text)
        return self

    def click_on_continue(self):
        btn_continue = self.driver.find_element(*self.__btn_continue)
        btn_continue.click()
        return ApplicationPersonalPage




