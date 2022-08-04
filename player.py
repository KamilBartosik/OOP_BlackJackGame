class Player:

    def __init__(self, balance=500):

        self.balance = balance

    def place_bet(self):

        while True:
            try:
                bet_amount = int(input('Place a bet: '))

            except:
                print(f'Please provide a number in range(0, {self.balance})')

            else:
                if self.balance >= bet_amount > 0:

                    self.balance -= bet_amount
                    print(f'Your bet: {bet_amount}$. Your actual balance: {self.balance}$.')
                    break

                else:
                    print(f'You do not have that amount of money, your balance is {self.balance}$!')

        return bet_amount

    def amount_of_bet(self, bet_amount):

        return bet_amount

    def add_money(self, amount):

        self.balance += int(amount)
        print(f'Your actual balance: {self.balance}$')

    def __str__(self):

        return f'Your actual balance: {self.balance}$'
