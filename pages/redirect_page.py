import allure

from locators.locators_main_page import ButtonRedirect
from locators.locators_redirect_page import RedirectLocators
from pages.base_page import BasePage


class RedirectPage(BasePage):

    @allure.step('Клик по лого Самокат в шапке')
    def click_scooter_logo(self):
        self.click_on_element(ButtonRedirect.SCOOTER_LOGO)

    @allure.step('Клик по лого Яндекс')
    def click_yandex_logo(self):
        self.click_on_element(ButtonRedirect.YANDEX_LOGO)

    @allure.step('Переход на главную Дзен')
    def find_button_element(self):
        return self.find_element_with_wait(RedirectLocators.DZEN_FIND_BUTTON)