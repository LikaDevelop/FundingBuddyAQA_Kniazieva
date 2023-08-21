from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from selenium import webdriver

from pages.MainPage import MainPage
from pages.OfferPage import OfferPage


@pytest.fixture(scope='class')
def chrome(request):
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    if request.cls:
        request.cls.driver = driver
    yield driver
    driver.quit()


