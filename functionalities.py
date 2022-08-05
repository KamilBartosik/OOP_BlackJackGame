def display(amount, balance, round_nb, player_cards, dealer_cards, values, state='end of the round'):

    print('\n'*10 + '-'*20)
    print('Blackjack game\n')
    print(f'Round {round_nb}')
    print(f'Your bet: {amount}$. Your actual balance: {balance}$.')

    if state == 'player_round':
        print(f'\nYour cards: ', *player_cards, sep='\n')
        print('')
        print(f'Dealer cards: \n{dealer_cards[0]} \nUNKNOWN')

    else:
        print('\nYour cards: ', *player_cards, sep='\n')
        print('')
        print('Dealer cards: ', *dealer_cards, sep='\n')
        print(f'\nYour score is {values()[0]}! \nDealer score is {values()[-1]}!')


def next_round():
    next_rnd = ''
    available_choices = ['yes', 'no']

    while next_rnd not in available_choices:

        next_rnd = input('Do you want to play next round (yes or no)?: ')

        if next_rnd not in available_choices:
            print("Please write your decision exactly as follows: 'yes' or 'no'")

    if next_rnd == 'yes':
        return True

    return False
