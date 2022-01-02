from enum import Enum


class Symbol(Enum):
    BEER = 1
    COFFEE = 2
    WINE = 3
    JOLLY = 4


class Card:

    def __init__(self, name, symbol, image):
        self.name = name
        self.symbol = symbol
        self.image = image

    def __eq__(self, other):
        if isinstance(other, Card):
            return self.name == other.name and self.symbol == other.symbol and self.jolly == other.jolly
        return False

    @property
    def name(self):
        return self._name

    @property
    def symbol(self):
        return self._symbol

    @property
    def image(self):
        return self._image

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) < 50:
            self._name = value
        else:
            raise "Card name is not correct"

    @symbol.setter
    def symbol(self, value):
        if isinstance(value, Symbol):
            self._symbol = value
        else:
            raise "Card symbol is not correct"

    @image.setter
    def image(self, value):
        self._image = value

    def jolly(self):
        if self._symbol == Symbol.JOLLY:
            return True
        return False
