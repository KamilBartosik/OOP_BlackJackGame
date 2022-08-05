from deck import Deck
from player import Player
from game_modules import GameModules
from functionalities import display, next_round, rules

rules('rules_description.txt')
print('\nWelcome to Blackjack Game!')
balance = 500
round_nb = 0

while True:

    round_nb += 1

    player = Player(balance)
    print(f'\n{player}')

    deck = Deck()
    deck.shuffle()

    player.place_bet()
    bet = player.bet_amount
    balance = player.balance

    player_cards = []
    dealer_cards = []

    player_cards.append(deck.take_card())
    dealer_cards.append(deck.take_card())
    player_cards.append(deck.take_card())
    dealer_cards.append(deck.take_card())

    game = GameModules(deck, player_cards, dealer_cards)

    display(bet, balance, round_nb, player_cards, dealer_cards, game.sum_value(), 'player_round')

    game.decision(bet, balance, round_nb)

    player.add_money(game.amount_of_bet)
    balance = player.balance

    if balance == 0:
        print(f'\nYou lost all of your money!\n\nGAME OVER')
        break

    if not next_round():
        print(f'\nThanks for playing! You played {round_nb} rounds and end up with: {balance}$ ({balance - 500}$ profit)')
        break
