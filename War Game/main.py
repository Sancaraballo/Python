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
            card = self._deck.take_draw()
            character.add_card(card)

    def start_battle(self, cards_from_war=None):
        print("Let's Start the Battle")

        player_card = self._player.deck.take_card()
        computer_card = self._computer.deck.take_card()

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
            computer_card = self._computer.draw_card()

            player_cards.append(player_card)
            computer_cards.append(computer_card)

        print('Six hidden cards: XXX XXX')
    
        self.start_battle(player_cards + computer_cards + cards_from_battle)

    def check_game_over(self):
        if self._player.has_empty_deck():
            print('Computer wins')
            return True
        elif self._computer.has_empty_deck():
            print('You are the winner, come again latter')
            return True
        else:
            return False
    
    def print_stats(self):
        print("\n----")
        print(f'You have {self._player.deck.size} cards on your deck,\
             whereas computer has {self._computer.deck.size}')
