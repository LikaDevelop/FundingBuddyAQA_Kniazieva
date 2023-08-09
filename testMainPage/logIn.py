from selenium.webdriver.common.by import By

class MainPage:

    def logIn(self, open_main_page):
        sign_in_locator = ".//a[@id = 'sign-in-btn' ]"
        sign_in_elements = open_main_page.find_elements(By.XPATH, sign_in_locator)
        sign_in_elements.click()
        pass








