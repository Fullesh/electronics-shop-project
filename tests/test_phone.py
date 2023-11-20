from src.phone import Phone

phone1 = Phone('iPhone 14', 120000, 5, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    assert str(phone1) == 'iPhone 14'


def test_add():
    assert phone1 + phone1 == 10
    assert phone1 + 2121 == 'Невозможно сложить с экземплярами не Phone или Item классов'



