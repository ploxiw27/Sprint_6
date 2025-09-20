import allure

from pages import main_page
from pages.main_page import MainPage
from pages.redirect_page import RedirectPage

@allure.title("Тестирование редиректа на главную страницу сайта")
class TestRedirectPage:
    def test_scooter_redirect(driver):
        order_page = MainPage(driver)
        order_page.open_url()

        with allure.step(f'Переход на главную страницу Самоката при клике на лого самокат'):
            order_page.click_scooter_logo()

            logo_page = RedirectPage(driver)
            logo_page.click_scooter_logo()
            assert logo_page.get_current_url() == main_page.get_current_url()

    @allure.title("Тестирование редиректа на главную страницу сайта Я.Дзен")
    def test_yandex_redirect(self):
        order_page = MainPage(self.driver)
        order_page.open_url()

        with allure.step('Проверка редиректа в Дзен по клику на Яндекс'): # Вызов нового окна
            redirect_dzen_page = RedirectPage(self.driver)
            redirect_dzen_page.click_yandex_logo()

            handles = self.driver.window_handles
            assert len(handles) == 2

            self.switch_to_new_window(handles[-1])

            redirect_dzen_page.find_element_find_button()
            final_url = redirect_dzen_page.get_current_url()

            assert 'https://dzen.ru/?yredirect=true' in final_url