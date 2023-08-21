from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.OfferPage import OfferPage


class MainPage:
    page_url = 'https://protest1.fun'

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__sign_in_locator = (By.XPATH, ".//a[@id = 'sign-in-btn' ]")
        self.__email_login_locator = (By.XPATH, ".//input[@class = 'landing_sign_in_email_input' and @placeholder = 'Email' ]")
        self.__password_login_locator = (By.XPATH, ".//input[@class = 'landing_sign_in_password_input' and @id = 'sign_in_pass_id' and @type = 'password' ]")
        self.__btn_sign_in_locator = (By.XPATH, ".//button[@class = 'landing_sign_in_form_btn']")

    def open(self) -> 'MainPage':
        self.driver.get(self.page_url)
        return self


    def click_on_sign_in(self):
        button = self.driver.find_element(*self.__sign_in_locator)
        button.click()
        return self

    def fill_in_email(self, email:str):
        field = self.driver.find_element(*self.__email_login_locator)
        field.send_keys(email)
        return self

    def fill_in_password(self, password:str):
        field = self.driver.find_element(*self.__password_login_locator)
        field.send_keys(password)
        return self

    def click_on_form_btn_sign_in(self):
        button = self.driver.find_element(*self.__btn_sign_in_locator)
        button.click()
        return OfferPage
