# War game Deck: 52 cards, Suits: 'Clubs', 'Diamond', 'Hearts' or 'Spades'
import Suit, Card

class Deck:
    _cards = []

    def build(self):
        for i in range(52):
            i = Card()
            if i not in self._cards:
                self._cards.append(Card())
    
    def shuffle(self):
        pass

    def show(self):
        pass
    
    def draw(self):
        pass