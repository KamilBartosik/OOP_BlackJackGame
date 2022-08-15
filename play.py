from deck import Deck
from player import Player
from game_modules import GameModules
from functionalities import display, next_round, rules


def play_game(rules_func):

    file_path = 'rules_description.txt'
    print('\nWelcome to Blackjack Game!')
    q_rules = rules_func(file_path)
    if q_rules == 'yes':

        print('\n' * 20 + '-' * 30)
        print('\nWelcome to Blackjack Game!')
        round_nb = 0
        player = Player()

        while True:

            round_nb += 1

            print(f'\n{player}')

            deck = Deck()
            deck.shuffle()
            player.place_bet()

            cards = [deck.take_card() for i in range(1, 5)]
            player_cards = [cards[0], cards[2]]
            dealer_cards = [cards[1], cards[3]]

            game = GameModules(deck, player_cards, dealer_cards)

            display(player.bet_amount, player.balance, round_nb, player_cards, dealer_cards, game.sum_value(), 'player_round')

            game.decision(player.bet_amount, player.balance, round_nb)
            player.add_money(game.amount_of_bet)

            if player.balance == 0:
                print(f'\nYou lost all of your money!\n\nGAME OVER')
                break

            if not next_round():
                print(
                    f'\nThanks for playing! You played {round_nb} rounds and end up with: {player.balance}$ ({player.balance - 500}$ profit)')
                break


if __name__ == '__main__':
    play_game(rules)
