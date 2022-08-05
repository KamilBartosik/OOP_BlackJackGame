def display(amount, balance, round_nb, player_cards, dealer_cards, values, state='end of the round'):
    # clear_output() -> later add something here to clear previous output
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
