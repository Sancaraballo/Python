import Card, Suit
import random

class Deck:

    SUIT = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, is_empty=False):
        self._cards = []

        if  not is_empty:
            self.buil()

    @property
    def size(self):
        return len(self._cards)

    def build(self):
        for suit in Deck.SUIT: 
            for value in range (2, 15):
                self._cards.append(Card(Suit(suit), value))
    
    def show(self):
        for card in self._cards:
            card.show()

    def shuffle(self):
        random.shuffle(self._cards)

    def take_card(self):
        if self._cards:
            return self._cards.pop()
        else:
            return None
    
    def add(self, card):
        self._cards.insert(0, card)