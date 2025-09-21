from datetime import date

import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators_main_page import ButtonRedirect
from locators.locators_order_page import OrderLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Клик по "Заказать" вверх, открываем форму заказа')
    def click_order_button_header(self, button: str) -> None:
        if button == 'button_hed':
            self.click_on_element(ButtonRedirect.BUTTON_ORDER_HEADER)
        elif button == 'button_page':
            self.scroll_to_element(ButtonRedirect.BUTTON_ORDER_LANDING)
            self.click_on_element(ButtonRedirect.BUTTON_ORDER_LANDING)

    @allure.step('Загрузка страницы Заказа, видно поле Имя')
    def name_field_element_wait(self) -> bool:
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.INPUT_NAME_FIELD))
        return self.find_element_with_wait(OrderLocators.INPUT_NAME_FIELD).is_enabled()

    @allure.step('Заполнить Имя')
    def fill_name_field(self, name: str) -> None:
        self.find_element_with_wait(OrderLocators.INPUT_NAME_FIELD).clear() # Сначала очищаем поле "запомнить"
        self.find_element_with_wait(OrderLocators.INPUT_NAME_FIELD).send_keys(name)

    @allure.step('Заполнить Фамилия')
    def fill_surname_field(self, surname: str) -> None:
        self.find_element_with_wait(OrderLocators.INPUT_SURNAME_FIELD).clear() # Очищаем поле
        self.find_element_with_wait(OrderLocators.INPUT_SURNAME_FIELD).send_keys(surname)

    @allure.step('Заполнить Адрес')
    def fill_address_field(self, address: str) -> None:
        self.find_element_with_wait(OrderLocators.INPUT_ADRESS_FIELD).clear() # Очищаем поле
        self.find_element_with_wait(OrderLocators.INPUT_ADRESS_FIELD).send_keys(address)

    @allure.step('Выбор станции Метро')
    def metro_station_select(self, station: str) -> None:
        self.click_on_element(OrderLocators.METRO_STATION_FIELD)
        self.find_element_with_wait(OrderLocators.METRO_STATION_FIELD).clear()
        self.find_element_with_wait(OrderLocators.METRO_STATION_FIELD).send_keys(station)


    @allure.step('Заполнить Телефон')
    def fill_phone_field(self, phone_number: str) -> None:
        self.find_element_with_wait(OrderLocators.PHONE_NUMBER_FIELD).clear() # Очистка поля
        self.find_element_with_wait(OrderLocators.PHONE_NUMBER_FIELD).send_keys(phone_number)

    @allure.step('Клик Далее, переход поп-ап форма Заказа')
    def click_next_button(self) -> None:
        self.click_on_element(OrderLocators.NEXT_BUTTON)

    @allure.step('Выбор даты Заказа')
    def date_order(self) -> None:
        calendar_field = self.find_element_with_wait(OrderLocators.CALENDAR)
        calendar_field.clear()
        calendar_field.send_keys(date)
        calendar_field.send_keys(Keys.ENTER)

    @allure.step('Выбрать срок Ренты')
    def rental_period(self) -> None:
        self.click_on_element(OrderLocators.RENTAL_DATE)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.FILL_DATE))
        self.click_on_element(OrderLocators.FILL_DATE)
        self.find_element_with_wait(OrderLocators.FILL_DATE).click()
        self.click_on_element(OrderLocators.FILL_DATE)

    @allure.step('Выбор цвета самоката')
    def colors_scooter(self) -> None:
        self.click_on_element(OrderLocators.COLOR_SCOOTER)

    @allure.step('Оставить коммент курьеру')
    def fill_comment_field(self, comment:str) -> None:
        comment_field = self.find_element_with_wait(OrderLocators.COMMENT)
        comment_field.clear() # Очищаем поле
        comment_field.send_keys(comment)


    @allure.step('Клик Заказать')
    def click_order_button_element(self) -> None:
        self.click_on_element(OrderLocators.ORDER)

    @allure.step('Подтверждение Заказа клик Да')
    def click_yes_button_element(self) -> None:
        self.click_on_element(OrderLocators.CONFIRM_YES)