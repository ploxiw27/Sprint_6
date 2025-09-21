import allure
import pytest

from data_tests.data import AnswerMain
from pages.main_page import MainPage

@allure.title("Проверка текста ответов на важные вопросы")
@pytest.mark.parametrize("question_num, expected_answers", AnswerMain.ANSWERS.items())
class TestMainPage:
    def test_main_page(driver, question_num, expected_answers):
        main_page = MainPage(driver)
        main_page.open_url()
        main_page.scroll_to_questions()


        with allure.step(f"Проверка вопроса {question_num}"):
            main_page.click_question(question_num)
            answer_txt = main_page.click_answer(question_num)

            assert answer_txt == expected_answers, f'Ответ для вопроса {question_num} не совпадает'