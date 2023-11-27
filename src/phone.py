from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        """
        Возвращает информацию об экземпляре класса
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Геттер для количества сим-карт
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Сеттер для количества сим-карт.
        Если количество сим-карт меньше или равно 0 тогда возвращается ошибка по количеству сим-карт.
        В ином случае присваивается переданное значение
        """
        if number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self._number_of_sim = number_of_sim
