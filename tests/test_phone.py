import pytest

from src.phone import Phone

phone1 = Phone('iPhone 14', 120000, 5, 2)


def test_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    assert phone1.number_of_sim == 2
    phone1.number_of_sim = 3
    assert phone1.number_of_sim == 3
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone1.number_of_sim = -1
        phone1.number_of_sim = 0


