from src import Card

import random


class Deck:

    def __init__(self, deck):
        self.deck = deck

    def __eq__(self, other):
        if not isinstance(other, Deck):
            raise TypeError("You must pass another Deck object")

        if len(self.deck) == len(other.deck):
            for i, s_card in enumerate(self.deck):
                if s_card != other.deck[i]:
                    return False

        return True

    @property
    def deck(self):
        return self._deck

    @deck.setter
    def deck(self, value):
        if isinstance(value, list) and all(isinstance(card, Card) for card in value):
            self._deck = value
        else:
            raise "Input cards are not of type Card"

    # def add_card(self, card):
    #     contain_card = self.deck.Contains(card)
    #     if isinstance(card, Card) and not contain_card:
    #         self.deck.append(card)
    #     else:
    #         raise "Input card is not of type Card"

    def print_deck(self):
        for card in self.deck:
            if card.jolly():
                print("Territorio:", card.name, "Simbolo: ", card.symbol, "This card is a jolly!")
            else:
                print("Territorio:", card.name, "Simbolo: ", card.symbol)

    def shuffle_deck(self):
        random.shuffle(self.deck)
