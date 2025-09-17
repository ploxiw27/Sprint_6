from selenium.webdriver.common.by import By
from data_tests.data import Person


class OrderLocators:

    INPUT_NAME_FIELD = (By.XPATH, '//div[2]/div[1]')
    INPUT_SURNAME_FIELD = (By.XPATH, '//div[2]/div[2]')
    INPUT_ADRESS_FIELD = (By.XPATH, '//div[2]/div[3]')
    METRO_STATION_FIELD = (By.XPATH, '//div[1]/input')
    PHONE_NUMBER_FIELD = (By.XPATH, '//div[2]/div[5]')
    NEXT_BUTTON = (By.XPATH, '//div[3]/button')
    CALENDAR = (By.XPATH, '//div[1]/div')
    SELECT_DATE = (By.XPATH, '//div[1]/div/input')
    RENTAL_DATE = (By.XPATH, '//div[1]/div[1]')
    FILL_DATE = (By.XPATH, '//div[2]/div[2]')
    COLOR_SCOOTER = (By.XPATH, f'//input[@id="{Person.random_color}"]')
    COMMENT = (By.XPATH, '/[2]/div[4]/input')
    ORDER = (By.XPATH, '//button[text()="Заказать"]')
    CONFIRM_YES = (By.XPATH, '//button[text()="Да"]')