from selenium.webdriver.common.by import By


class QuestionMain:

    QUESTION_BUTTON = (By.ID, "accordion__heading-{}")
    QUESTION_8 = (By.XPATH, "//div/div[8]")

class AnswerQuestion:

    ANSWER_QUESTION = (By.ID, "accordion__panel-{}")

class ButtonRedirect:

    BUTTON_ORDER_HEADER = (By.XPATH, "//div[2]/button[1]")
    BUTTON_ORDER_LANDING = (By.XPATH, "//div[5]/button")
    SCOOTER_LOGO = (By.XPATH, "//div[1]/a[2]")
    YANDEX_LOGO = (By.XPATH, "//div[1]/a[1]")
