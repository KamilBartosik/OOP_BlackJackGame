class Player:

    def __init__(self, balance=500, bet_amount=0):

        self.balance = balance
        self.bet_amount = bet_amount

    def place_bet(self):

        while True:
            try:
                self.bet_amount = int(input('Place a bet: '))

            except:
                print(f'Please provide a number in range(0, {self.balance})')

            else:
                if self.balance >= self.bet_amount > 0:

                    self.balance -= self.bet_amount
                    print(f'Your bet: {self.bet_amount}$. Your actual balance: {self.balance}$.')
                    break

                else:
                    print(f'You do not have that amount of money, your balance is {self.balance}$!')

    def add_money(self, amount):

        self.balance += int(amount)
        print(f'Your actual balance: {self.balance}$')

    def __str__(self):

        return f'Your actual balance: {self.balance}$'
