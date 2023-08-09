from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest


@pytest.fixture(scope='class')
def open_main_page():
    my_service = Service(executable_path=ChromeDriverManager().install())
    driver = Chrome(service=my_service)
    driver.get('https://protest1.fun')
    yield driver
    driver.quit()
