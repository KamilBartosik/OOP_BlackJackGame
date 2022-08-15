def display(amount, balance, round_nb, player_cards, dealer_cards, values, state='end of the round'):

    print('\n'*10 + '-'*30)
    print('Blackjack game\n')
    print(f'Round {round_nb}')
    print(f'Your bet: {amount}$. Your actual balance: {balance}$.')

    if state == 'player_round':
        print(f'\nYour cards: ', *player_cards, sep='\n')
        print(f'\nDealer cards: \n{dealer_cards[0]} \nUNKNOWN')

    else:
        print('\nYour cards: ', *player_cards, sep='\n')
        print('\nDealer cards: ', *dealer_cards, sep='\n')
        print(f'\nYour score is {values()[0]}! \nDealer score is {values()[-1]}!')


def next_round():

    choices = ['yes', 'no']

    while True:
        next_rnd = input('Do you want to play next round (yes or no)?: ')

        if next_rnd in choices:
            break
        else:
            print("\nPlease write your decision exactly as follows: 'yes' or 'no'")

    if next_rnd == 'yes':
        return True

    return False


def rules(file_path):

    choices = ['yes', 'no']

    while True:
        familiar = input("\nAre you familiar with the rules of the game? (yes or no): ")

        if familiar in choices:
            break
        else:
            print("Please write 'yes' or 'no'")

    if familiar == 'no':
        with open(file_path, 'r') as f:
            lines = f.read()
            print(lines)

        while True:
            ready = input("\nReady to play? (yes or no): ")

            if ready not in choices:
                print("Please type 'yes' or 'no'")

            else:
                break
    else:
        ready = 'yes'

    if ready == 'no':
        print("\nToo bad :(\nSee you some other time!")

    return ready
