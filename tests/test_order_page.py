import allure
import pytest

from data_tests.data import Person
from pages.order_page import OrderPage

@allure.title('Проверка заказа самоката, появление окон заказа')
@pytest.mark.parametrize('button', ['button_header', 'button_page'])
class TestOrderPage:

    def test_order_page(self, driver, button):
        order_page = OrderPage(driver)
        order_page.open_url()

        person = Person() # Генератор данных


        with allure.step(f'Заказ самоката через верхнюю кнопку {button}'):
            order_page.click_order_button_header(button=button)
            order_page.name_field_element_wait()

            order_page.fill_name_field(person.random_name) # Используем сгенерированное имя
            order_page.fill_surname_field(person.random_surname) # Используем сгенерированную фамилию
            order_page.fill_address_field(person.address)  # Используем сгенерированный адрес
            order_page.metro_station_select(person.random_station())  # Передаем сгенерированную станцию из списка
            order_page.fill_phone_field(person.random_phone_number) # Передаем сгенерированный номер телефона
            order_page.fill_comment_field(person.comment)  # Передаем сгенерированный комментарий из списка
            order_page.click_next_button() # Клик Далее
            order_page.date_order(person.random_date)  # Передаем сгенерированную дату
            order_page.rental_period()
            order_page.colors_scooter()
            order_page.click_order_button_element()
            order_page.click_yes_button_element()