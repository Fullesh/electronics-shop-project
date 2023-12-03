import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """
        Возвращает описание экземпляра класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        Возвращает название товара
        """
        return f'{self.name}'

    def __add__(self, other):
        """
        Возвращает сложенные значения количества из классов
        В случае непринадлежности классов друг к другу возвращает ошибку
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return 'Невозможно сложить с экземплярами не Phone или Item классов'

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @property
    def get_name(self):
        """
        Геттер для имени товара
        """
        return self.name

    @get_name.setter
    def set_name(self, product_name_str):
        """
        Сеттер для имени товара.
        В случае если длина товара превышает 10 символов, то присваиваются первые 10 символов
        В ином случае присваевается полное название товара.
        """
        if len(product_name_str) > 10:
            print('Длина наименования товара превышает 10 символов')
            self.name = product_name_str[:10]
        else:
            self.name = product_name_str

    @staticmethod
    def string_to_number(number_string):
        """
        Возвращает преобрщованное строковое значение в число с плавающей запятой
        """
        return int(float(number_string))

    @classmethod
    def instantiate_from_csv(cls, file_csv: str = None) -> None:
        """
        Инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        """
        if file_csv is None:
            raise FileNotFoundError('Отсутствует файл item.csv')
        try:
            base_path = os.path.dirname(__file__)
            file_path = os.path.join(base_path, file_csv)

            cls.all.clear()

            with open(file_path, newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    Item(row['name'], float(row['price']), int(row['quantity']))
        except KeyError:
            raise InstantiateCSVError


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        super().__init__(message)
