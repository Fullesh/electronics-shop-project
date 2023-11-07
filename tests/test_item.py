"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Телефон", 60000, 20)
item2 = Item("Ноутбук", 28000, 5)


def test_item():
    assert item1.calculate_total_price() == 1200000
    assert item2.calculate_total_price() == 140000
    assert Item.all == ['Телефон', 'Ноутбук']
    Item.pay_rate = 0.8
    assert item1.apply_discount() == 48000.0
