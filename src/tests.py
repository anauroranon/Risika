from src import *
from unittest import TestCase


class risika_tests(TestCase):

    def test_card(self):
        card1 = Card("Psicologia", Symbol.WINE, True)
        card2 = Card("Informatica", Symbol.BEER, True)
        card3 = Card("Psicologia", Symbol.WINE, True)

        self.assertEqual(card1, card1)
        self.assertEqual(card1, card3)
        self.assertNotEqual(card1, card2)
        self.assertIsInstance(card1, Card)
        self.assertEqual(card3.name, "Psicologia")

    def test_full_decl(self):
        d = initialize_deck()
        d1 = Deck([Card("Lingue", Symbol.COFFEE),
                 Card("Giurisprudenza", Symbol.COFFEE),
                 Card("Infermieristica", Symbol.COFFEE),
                 Card("Medicina", Symbol.COFFEE),
                 Card("Tossicologia", Symbol.COFFEE),
                 Card("Scienze della natura", Symbol.COFFEE),
                 Card("Ingegneria Chimica", Symbol.COFFEE),
                 Card("Ingegneria Elettronica", Symbol.COFFEE),
                 Card("Fisica", Symbol.COFFEE),
                 Card("Matematica", Symbol.COFFEE),
                 Card("Chimica", Symbol.COFFEE),
                 Card("Architettura", Symbol.COFFEE),
                 Card("Filosofia", Symbol.BEER),
                 Card("Lettere", Symbol.BEER),
                 Card("Scienze politiche", Symbol.BEER),
                 Card("Scienze motorie", Symbol.BEER),
                 Card("Biologia", Symbol.BEER),
                 Card("Ingegneria meccanica", Symbol.BEER),
                 Card("Ingegneria Civile", Symbol.BEER),
                 Card("Informatica", Symbol.BEER),
                 Card("Psicologia", Symbol.WINE),
                 Card("Pedagogia", Symbol.WINE),
                 Card("Economia", Symbol.WINE),
                 Card("Odontoiatria", Symbol.WINE),
                 Card("CTF", Symbol.WINE),
                 Card("Farmacia", Symbol.WINE)])

        self.assertEqual(d, d1)
        self.assertIsInstance(d, Deck)
        for c in d.deck:
            self.assertIsInstance(c, Card)


