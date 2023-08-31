from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages import EntityTypePage, OfferPage


class MainPage:
    page_url = 'https://protest1.fun'

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.__sign_in_locator = (By.CSS_SELECTOR, 'a.landing_sign_in_btn')
        self.__email_login_locator = (By.CSS_SELECTOR, 'input.landing_sign_in_email_input')
        self.__password_login_locator = (By.CSS_SELECTOR, 'input.landing_sign_in_password_input')
        self.__btn_sign_in_locator = (By.CSS_SELECTOR, 'button.landing_sign_in_form_btn')
        self.__btn_apply_now_locator = (By.CSS_SELECTOR, 'button#applyNowButton')
        self.__canadian_flag = (By.CSS_SELECTOR, 'button#ca')

    def open(self) -> 'MainPage':
        self.driver.get(self.page_url)
        return self

    def click_on_sign_in(self):
        button = self.driver.find_element(*self.__sign_in_locator)
        button.click()
        return self

    def fill_in_email(self, email: str):
        field = self.driver.find_element(*self.__email_login_locator)
        field.send_keys(email)
        return self

    def fill_in_password(self, password: str):
        field = self.driver.find_element(*self.__password_login_locator)
        field.send_keys(password)
        return self

    def click_on_form_btn_sign_in(self):
        button = self.driver.find_element(*self.__btn_sign_in_locator)
        button.click()
        return OfferPage

    def click_on_apply_now(self):
        button = self.driver.find_element(*self.__btn_apply_now_locator)
        button.click()
        return EntityTypePage

    def click_canadian_flag(self):
        flag = self.driver.find_element(*self.__canadian_flag)
        flag.click()
        return self

