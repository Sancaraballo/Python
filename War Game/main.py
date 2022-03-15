# War game Deck: 52 cards, Suits: 'Clubs', 'Diamond', 'Hearts' or 'Spades'


class WarCardGame:

    PLAYER = 0
    COMPUTER = 1
    TIE = 2

    def __init__(self, player, computer, deck):
        self._player = player
        self._computer = computer
        self._deck = deck
    
    def make_initial_deck(self):
        self._deck.shuffle()
        self.make_deck(self._player)
        self.make_deck(self._computer)

    def make_deck(self, character):
        for i in range(26):
            card = self._deck.draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("Let's Start the Battle")

        player_card = self._player_deck.draw_card()
        computer_card = self._computer.deck.draw_card()

        print('Your Card:')
        player_card.show()

        print('\nComputer Card:')
        computer_card.show()

        winner = self.get_round_winner(player_card, computer_card)
        cards_won = self.get_cards_won(player_card, computer_card, cards_from_war)

        if winner = WarCardGame.PLAYER:
            print("\n You won this round!")
            self.add_cards_to_character(self._player, cards_won)
        elif winner = WarCardGame.COMPUTER:
            print('\n The Computer won this round')
            self.add_cards_to_character(self._computer, cards_won)
        else:
            print("\n It's a tie. The war started!")
            self.start_war(cards_won)
        
        return winner

    
    def get_round_winner(self, player_card, computer_card):
        if player_card.value > computer_card.value:
            return WarCardGame.PLAYER
        elif player_card.value < computer_card.value:
            return WarCardGame.COMPUTER
        else:
            return WarCardGame.TIE

    def get_card_won(self, player_card, computer_card, previous_cards):
        if previous_cards: 
            return [player_card, computer_card] + previous_cards
        else:
            return [computer_card, player_card]    

    def add_cards_to_character(self, character, lst_cards):
        for card in lst_cards:
            character.add_card(card)
        
    def start_war(self, cards_from_battle):
        player_cards = []
        computer_cards = []

        for i in range(3):
            player_card = self._player.draw_card()