import pytest

from src.keyboard import Keyboard

kb = Keyboard('Crosshair Pro 10', 10000, 10)


def test_get_name():
    assert str(kb) == "Crosshair Pro 10"


def test_get_lang():
    assert str(kb.language) == 'EN'


def test_change_lang():
    kb.change_lang()
    assert str(kb.language) == 'RU'


def test_exception():
    with pytest.raises(AttributeError, match="property 'language' of 'Keyboard' object has no setter"):
        kb.language = 'EU'
