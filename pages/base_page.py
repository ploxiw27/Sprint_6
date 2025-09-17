import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from curls import main_site
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    MAIN_URL = main_site

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 12)

    @allure.step('Открываем главную страницу')
    def open_url(self):
        self.driver.get(self.MAIN_URL)


    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)


    @allure.step('Поиск элемента')
    def find_element_with_wait(self, locator):
        return self.wait.until(EC.visibility_of_element_located(*locator))

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        element = self.find_element_with_wait(*locator)
        element.click()

    @allure.step("Получение текста элемента")
    def get_text_to_element(self, locator):
        element = self.find_element_with_wait(*locator)
        return element.text


    @allure.step('Возврат страницы в исходное')
    def get_current_url(self):
        return self.driver.current_url


    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self, window_handle):
        self.driver.switch_to.window(window_handle)


