import allure
import pytest
from pages.order_page import OrderPage

@allure.title('Проверка заказа самоката, появление окон заказа')
@pytest.mark.parametrize('button', ['button_header', 'button_page'])
class TestOrderPage():
    def test_order_page(driver, button):
        order_page = OrderPage(driver)
        order_page.open_url()

        with allure.step(f'Заказ самоката через верхнюю кнопку {button}'):
            order_page.click_order_button_header(button=button)
            order_page.name_field_element_wait()
            order_page.fill_name_field()
            order_page.fill_surname_field()
            order_page.fill_adress_field()
            order_page.metro_station_select()
            order_page.fill_phone_field()
            order_page.click_next_button()
            order_page.date_order()
            order_page.rental_period()
            order_page.colors_scooter()
            order_page.fill_comment_field()
            order_page.click_order_button_element()
            order_page.click_yes_button_element()