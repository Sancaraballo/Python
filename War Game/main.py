# War game Deck: 52 cards, Suits: 'Clubs', 'Diamond', 'Hearts' or 'Spades'


class Suit:
    description = ["clubs", "diamonds", "hearts", "spades"]
    symbol = ["♣", "♦", "♥", "♠"]



class Card:
    suit = Suit()
    
    value = ''

    def show(self):
        return self.value

    def is_special(self):
        return self.value in [11, 12, 13, 14]

class Deck:
    _cards = Card()
