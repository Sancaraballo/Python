import Suit, Card

class Deck:

    SUIT = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, is_empty=False):
        self._cards = []

    
    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUIT: 
            for value in range (2, 15):
                self._cards.append(Card(Suit(suit), value))