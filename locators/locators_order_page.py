from selenium.webdriver.common.by import By

from data_tests.data import Person


class OrderLocators:

    INPUT_NAME_FIELD = (By.XPATH, "//input[@type='text' and @placeholder='* Имя']")
    INPUT_SURNAME_FIELD = (By.XPATH, "//input[@type='text' and @placeholder='* Фамилия']")
    INPUT_ADRESS_FIELD = (By.XPATH, "//input[@type='text' and @placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION_FIELD = (By.XPATH, "//input[@tabindex='0' and @placeholder='* Станция метро']")
    PHONE_NUMBER_FIELD = (By.XPATH, "//input[@type='text' and @placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    CALENDAR = (By.XPATH, "//input[@value='' and @placeholder='* Когда привезти самокат']")
    RENTAL_DATE = (By.XPATH, "//div[contains(@class, 'Dropdown-arrow-wrapper')]//span[contains(@class, 'Dropdown-arrow')]")
    FILL_DATE = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and contains(text(), 'четверо суток')]")
    COLOR_SCOOTER = (By.XPATH, '//input[@id="{color}"]')
    COMMENT = (By.XPATH, "//input[@type='text' and @placeholder='Комментарий для курьера']")
    ORDER = (By.XPATH, '//button[text()="Заказать"]')
    CONFIRM_YES = (By.XPATH, '//button[text()="Да"]')