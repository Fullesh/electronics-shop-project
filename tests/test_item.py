"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Телефон", 60000, 20)
item2 = Item("Ноутбук", 28000, 5)


def test_calculate_total_price():
    assert Item.calculate_total_price(item1) == 1200000


def test_apply_discout():
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 48000


def test_string_to_number():
    assert Item.string_to_number('10.0') == 10
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.5') == 10


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    item2 = Item.all[0]
    assert item2.name == 'Смартфон'
    assert len(item2.all) == 5


def test_set_name():
    item1.name = 'Notebook'
    assert item1.name == 'Notebook'
