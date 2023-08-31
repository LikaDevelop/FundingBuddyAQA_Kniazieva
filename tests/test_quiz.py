import pytest
from pages.AutodeclinePage import AutodeclinePage
from pages.CreditScore import CreditScore
from pages.EntityTypePage import EntityTypePage
from pages.LendingAmout import LendingAmount
from pages.LendingPurpose import LendingPurpose
from pages.MainPage import MainPage
from pages.RegistrationPage import RegistrationPage


@pytest.mark.usefixtures('chrome')
class TestQuiz:

    def test_autodecline_first_low_credit_score(self):
        main_page = MainPage(self.driver)
        main_page.open()\
                 .click_on_apply_now()
        entity_page = EntityTypePage(self.driver)
        entity_page.chose_answer_i_dont_own_business_yet()
        credit_score_page = CreditScore(self.driver)
        credit_score_page.choose_answer_below_500()
        autodecline_page = AutodeclinePage(self.driver)
        assert autodecline_page.check_go_to_autodecline()

    def test_back_to_credit_score(self):
        main_page = MainPage(self.driver)
        main_page.open() \
            .click_on_apply_now()
        entity_page = EntityTypePage(self.driver)
        entity_page.chose_answer_i_dont_own_business_yet()
        credit_score_page = CreditScore(self.driver)
        credit_score_page.choose_answer_700()
        lending_amount = LendingAmount(self.driver)
        lending_amount.click_on_the_btn_back()
        assert credit_score_page.check_is_redirect_to_credit_score()

    def test_back_and_rechoose_to_credit_score(self):
        main_page = MainPage(self.driver)
        main_page.open() \
            .click_on_apply_now()
        entity_page = EntityTypePage(self.driver)
        entity_page.chose_answer_i_dont_own_business_yet()
        credit_score_page = CreditScore(self.driver)
        credit_score_page.choose_answer_700()
        lending_amount = LendingAmount(self.driver)
        lending_amount.click_on_the_btn_back()
        credit_score_page.rechoose_answer_651()
        credit_score_page.select_answer_651()
        assert lending_amount.check_is_redirect()



    def test_go_to_personal_registration(self):
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

        assert registration_page.check_is_redirect_to_registration_form()











