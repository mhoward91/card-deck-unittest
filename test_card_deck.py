import unittest
from card_deck import Card, Deck


class CardTests(unittest.TestCase):

    # an instance of the Card class is created prior to running the Card tests
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """each card has a suit & value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """each card returns its correct string representation"""
        self.assertEqual(repr(self.card), "A of Hearts")


class DeckTests(unittest.TestCase):

    # an instance of the Deck class (a full deck of cards) is created prior to running the Deck tests
    def setUp(self):
        self.deck = Deck()

    def test_init(self):
        """each deck is a python list of 52 unique cards"""
        self.assertTrue(isinstance(self.deck.cards, list))
        self.assertEqual(len(self.deck.cards), 52)

    def test_count(self):
        """count should return a count of the number of cards in the deck"""
        self.assertEqual(self.deck.count(), 52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(), 51)

    def test_deal(self):
        """_deal should deal the number of cards specified, to a new list"""
        cards = self.deck._deal(10)
        self.assertEqual(len(cards), 10)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_no_cards(self):
        """an empty deck cannot be dealt"""
        self.deck.cards = []
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """deal_card should deal a single card from the deck"""
        card = self.deck.cards[-1]
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card)
        self.assertEqual(self.deck.count(), 51)

    def test_deal_hand(self):
        """deal_hand should deal the number of cards passed to the arg"""
        cards = self.deck.deal_hand(20)
        self.assertEqual(len(cards), 20)
        self.assertEqual(self.deck.count(), 32)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(cards, self.deck.cards)


if __name__ == "__main__":
    unittest.main()
