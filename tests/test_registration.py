import pytest

from pages.ApplicationPersonalPage import ApplicationPersonalPage
from pages.AutodeclinePage import AutodeclinePage
from pages.CreditScore import CreditScore
from pages.EntityTypePage import EntityTypePage
from pages.LendingAmout import LendingAmount
from pages.LendingPurpose import LendingPurpose
from pages.MainPage import MainPage
from pages.RegistrationPage import RegistrationPage


@pytest.mark.usefixtures('chrome')
class TestRegistration:
    def test_personal_registration(self):
        main_page = MainPage(self.driver)
        main_page.open() \
            .click_on_apply_now()
        entity_page = EntityTypePage(self.driver)
        entity_page.chose_answer_i_dont_own_business_yet()
        credit_score_page = CreditScore(self.driver)
        credit_score_page.choose_answer_700()
        lending_amount = LendingAmount(self.driver)
        lending_amount.choose_answer_5000_10000()
        lending_purpose = LendingPurpose(self.driver)
        lending_purpose.choose_answer_advertising()
        registration_page = RegistrationPage(self.driver)
        registration_page.fill_in_full_name('Test Personal Autotest')
        registration_page.full_in_email('testtost12345678+01002@gmail.com')
        registration_page.full_in_cell_phone('8329017842')
        registration_page.full_in_password('qwerty123QWERTY')
        registration_page.click_on_continue()

        application_personal_page = ApplicationPersonalPage(self.driver)
        assert application_personal_page.check_is_redirect()





