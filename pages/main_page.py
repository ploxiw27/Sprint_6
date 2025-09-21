import allure

from locators.locators_main_page import AnswerQuestion
from locators.locators_main_page import ButtonRedirect
from locators.locators_main_page import QuestionMain
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Скролл до важных вопросов')
    def scroll_to_questions(self):
        self.scroll_into_view(QuestionMain.QUESTION_8)

    @allure.step('Клик по вопросу')
    def click_question(self, question_num):
        formatted_questions_locator = self.format_locator(QuestionMain.QUESTION_BUTTON, question_num)
        self.click_on_element(formatted_questions_locator)

    @allure.step('Получение текста ответа')
    def click_answer(self, answer_num):
        formatted_answer_locator = self.format_locator(AnswerQuestion.ANSWER_QUESTION, answer_num)
        return self.get_text_from_element(formatted_answer_locator)

    @allure.step('Клик "Заказать" вверху страницы')
    def click_order_button(self):
        self.click_on_element(ButtonRedirect.BUTTON_ORDER_HEADER)