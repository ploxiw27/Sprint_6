from russian_names import RussianNames
import random

class AnswerMain:
    ANSWERS = {
        0: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        1: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        2: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        3: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        4: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        5: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        6: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        7: 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    }

class Person: # Генерация случайного пользователя с русским именем Имя Фамилия Адрес Цвет самоката
    generator = RussianNames()
    full_name = generator.get_person()
    random_name = full_name.split()[0]
    random_surname = full_name.split()[2]
    random_phone_number = f"+7{random.randint(900, 999)}{random.randint(100, 999)}{random.randint(1001, 9999)}"
    random_date = f"{random.randint(1, 28)}"
    current_period_name = ["сутки", "двое суток", "трое суток"]
    random_period = f"{random.choice(current_period_name)}"
    current_station_list = ["Первомайская", "Измайловская", "Партизанская", "Киевская"]
    random_station = f"{random.choice(current_station_list)}"
    colors = ["black", "grey"]
    random_color = f"{random.choice(colors)}"

    def fill_adress_field(self):
        current_street_name = ["Первомайская", "Ленина", "Маяковского", "Парковая", "Заводская", "Пушкина", "Плащадь"]
        street = random.choice(current_street_name)
        house = random.randint(1, 100)
        flat = random.randint(1, 100)
        self.adress = f"Москва, {street}, {house}, {flat}"

    def fill_comment_field(self):
        current_words = ["Хочется с колесами", "Хочу с рулем", "Можно без сиденья"]
        words = random.choice(current_words)
        numbers = random.randint(100, 1000)
        self.comment =f"Комментарий, {words}, {numbers}"
