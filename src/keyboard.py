from src.item import Item


class MixinLang:
    def __init__(self):
        self._language = 'EN'

    def change_lang(self):
        if self._language in ('EN', 'En', 'eN', 'en'):
            self._language = 'RU'
        elif self._language in ('RU', 'Ru', 'rU', 'ru'):
            self._language = 'EN'
        else:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        return self


class Keyboard(Item, MixinLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language
