import random

from russian_names import RussianNames


class AnswerMain:
    ANSWERS = {
        0: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        1: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        2: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        3: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        4: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        5: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        6: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        7: 'Да, обязательно. Всем самокатов! И в Москве, и Московской области.'
    }

class Person:

    def __init__(self):
        self.generator = RussianNames()
        self.full_name = self.generator.get_person()
        self.random_name = self.full_name.split()[0]  # Генерируем имя
        self.random_surname = self.full_name.split()[2]  # Генерируем фамилию
        self.random_phone_number = self.generate_random_phone_number()
        self.random_date = self.generate_random_date()
        self.random_period = self.generate_random_rental_period()
        self.random_station = self.generate_random_station()
        self.random_color = self.generate_random_color()
        self.address = self.fill_address()  # Генерируем адрес сразу
        self.comment = self.fill_comment()  # Генерируем комментарий сразу

    def generate_random_phone_number(self) -> str:
        return f"+7{random.randint(900, 999)}{random.randint(100, 999)}{random.randint(1000, 9999)}"

    def generate_random_date(self) -> str:
        return str(random.randint(1, 28))

    def generate_random_rental_period(self) -> str:
        current_period_name = ["сутки", "двое суток", "трое суток", "четверо суток", "пятеро суток", "шестеро суток", "семеро суток"]
        return random.choice(current_period_name)

    def generate_random_station(self) -> str:
        current_station_list = ["Первомайская", "Измайловская", "Партизанская", "Киевская"]
        return random.choice(current_station_list)

    def generate_random_color(self) -> str:
        colors = ["black", "grey"]
        return random.choice(colors)

    def fill_address(self) -> str:
        current_street_name = ["Первомайская", "Ленина", "Маяковского", "Парковая", "Заводская", "Пушкина", "Площадь"]
        street = random.choice(current_street_name)
        house = random.randint(1, 100)
        flat = random.randint(1, 100)
        return f"Москва, {street}, {house}, {flat}"

    def fill_comment(self) -> str:
        current_words = ["Хочется с колесами", "Хочу с рулем", "Можно без сиденья"]
        words = random.choice(current_words)
        numbers = random.randint(100, 1000)
        return f"Комментарий: {words}, {numbers}"