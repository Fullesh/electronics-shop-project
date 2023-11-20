import csv


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
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
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
        return self.name

    @get_name.setter
    def set_name(self, product_name_str):
        if len(product_name_str) > 10:
            print('Длина наименования товара превышает 10 символов')
            self.name = product_name_str[:10]
        else:
            self.name = product_name_str

    @staticmethod
    def string_to_number(number_string):
        return int(float(number_string))

    @classmethod
    def instantiate_from_csv(cls, directory):
        cls.all.clear()
        with open(directory, 'r') as csv_file:
            file = csv.DictReader(csv_file)
            for i in file:
                name = i['name']
                price = float(i['price'])
                quantity = int(i['quantity'])
                item = cls(str, float, int)
                item.name = name
                item.price = price
                item.quantity = quantity
                cls.all.append(item)
