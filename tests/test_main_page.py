import pytest
from pages.MainPage import MainPage

from pages.OfferPage import OfferPage

user1_data = {'email': 'testtost12345678+01001@gmail.com',
              'password': 'qwerty123QWERTY'}

@pytest.mark.usefixtures('chrome')
class TestMainPage:
    def test_log_in(self):
        main_page = MainPage(self.driver)
        main_page.open() \
            .click_on_sign_in().fill_in_email(user1_data.get('email')) \
            .fill_in_password(user1_data.get('password')) \
            .click_on_form_btn_sign_in()
        offer_page = OfferPage(self.driver)
        assert offer_page.check_log_in()
