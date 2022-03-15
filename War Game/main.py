import Deck, Player, Game

player = Player.Player('Santi', Deck.Deck(is_empty=True))
computer = Player.Player('CPU', Deck.Deck(is_empty=True), is_computer=True)
deck = Deck.Deck()

game = Game.WarCardGame(player, computer, deck)

while not game.check_game_over():
    game.start_battle()
    game.print_stats()

    answer = input("Are you ready for next round? \
                    Press Enter to continue. \
                    Press Esc to finish the game")
    
    if answer.lower() == "Esc":
        break