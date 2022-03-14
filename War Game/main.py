# War game Deck: 52 cards, Suits: 'Clubs', 'Diamond', 'Hearts' or 'Spades'

class Suit:

    SYMBOLS = {"clubs":"♣", "diamonds":"♦", "hearts":"♥", "spades":"♠"}

    def __init__(self, description):
        self._description = description
        self._symbol = Suit.SYMBOLS[description]

    @property
    def description(self):
        return self._description
    
    @property
    def symbol(self):
        return self._symbol

class Card:
    suit = Suit()
    
    value = ''

    def show(self):
        return self.value

    def is_special(self):
        return self.value in [11, 12, 13, 14]

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