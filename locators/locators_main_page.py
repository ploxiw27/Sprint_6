from selenium.webdriver.common.by import By


class QuestionMain:

    QUESTION_BUTTON = (By.XPATH, "//div[contains(text(), 'Сколько это стоит?')]")
    QUESTION_8 = (By.XPATH, "//div[@role='button' and @aria-controls='accordion__panel-15']")

class AnswerQuestion:

    ANSWER_QUESTION = (By.ID, "//div[contains(@class, 'accordion__panel') and contains(., 'Сутки — 400 рублей')]")

class ButtonRedirect:

    BUTTON_ORDER_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button')]")
    BUTTON_ORDER_LANDING = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(@class, 'Button_Middle')]")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR') and img[@alt='Scooter']]")
    YANDEX_LOGO = (By.XPATH, "//a[img[@alt='Yandex']]")