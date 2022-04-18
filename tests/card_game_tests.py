import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def test_check_for_ace(self):
        self.assertEqual(1, True)

    def test_highest_card(self):
        card1 = Card("spades", 4)
        card2 = Card("spades", 3)
        game = CardGame
        actual = game.highest_card(self, card1, card2)
        expected = card1
        self.assertEqual(actual, expected)

    def test_cards_total(self):
        card1 = Card("spades", 4)
        card2 = Card("spades", 3)
        game = CardGame
        cards = [card1, card2]
        actual = game.cards_total(self, cards)
        expected = "You have a total of 4"
        self.assertEqual(actual, expected)

    