import allure
import pytest

from data_tests.data import Person
from pages.order_page import OrderPage



@pytest.mark.parametrize('button', ['button_header', 'button_page'])
class TestOrderPage:

    @allure.title('Проверка заказа самоката, появление окон заказа')
    def test_order_page(self, driver, button):
        order_page = OrderPage(driver)
        order_page.open_url()
        person = Person() # Генератор данных
        color = person.random_color

        with allure.step(f'Заказ самоката через верхнюю кнопку {button}'):
            order_page.click_order_button_header(button=button)
            order_page.name_field_element_wait()

            order_page.fill_name_field(person.random_name) # Используем сгенерированное имя
            order_page.fill_surname_field(person.random_surname) # Используем сгенерированную фамилию
            order_page.fill_address_field(person.address)  # Используем сгенерированный адрес
            order_page.metro_station_select(person.random_station)  # Передаем сгенерированную станцию из списка
            order_page.fill_phone_field(person.random_phone_number)
            order_page.fill_comment_field(person.comment)  # Передаем сгенерированный комментарий из списка
            order_page.click_next_button()
            order_page.date_order(person.random_date)
            order_page.rental_period()
            order_page.colors_scooter()
            order_page.click_order_button_element()
            order_page.click_yes_button_element()

            with allure.step('Проверка pop-up окна о создании заказа'):
                assert order_page.is_success_popup_displayed()

                success_message = order_page.get_success_message()
                assert success_message is not None

                assert "Заказ оформлен" in success_message