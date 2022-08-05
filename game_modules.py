from display import display


class GameModules:

    def __init__(self, deck, player_cards, dealer_cards):

        self.deck = deck
        self.player_cards = player_cards
        self.dealer_cards = dealer_cards

    def sum_value(self):

        person_start_sum = 0

        def person_sum_value(person_sum, person_cards):
            for i in person_cards:
                if i.value == [1, 11]:
                    person_sum += i.value[0]

                else:
                    person_sum += i.value

            for i in person_cards:
                if i.rank == 'Ace' and person_sum < 12:
                    person_sum += 10

            return person_sum

        player_sum = person_sum_value(person_start_sum, self.player_cards)
        dealer_sum = person_sum_value(person_start_sum, self.dealer_cards)

        return player_sum, dealer_sum

    def decision(self, amount_of_bet, balance, round_nb):

        self.amount_of_bet = amount_of_bet

        while True:
            try:
                dec = input("What is your move (hit or stand): ")

            except:
                print("Wrong move! Please input 'hit' or 'stand'")

            else:
                if dec == 'stand':
                    if self.sum_value()[-1] < 17:
                        self.dealer_cards.append(self.deck.take_card())
                    else:
                        break

                else:
                    self.player_cards.append(self.deck.take_card())
                    display(amount_of_bet, balance, round_nb, self.player_cards, self.dealer_cards, self.sum_value, 'player_round')

                    if self.sum_value()[0] > 21:
                        display(amount_of_bet, balance, round_nb, self.player_cards, self.dealer_cards, self.sum_value)
                        print('\nYou lost')
                        self.amount_of_bet = 0
                        break

        display(amount_of_bet, balance, round_nb, self.player_cards, self.dealer_cards, self.sum_value)
        if self.sum_value()[0] == 21 > self.sum_value()[-1] and len(self.player_cards) == 2:
            print('\nBLACKJACK! You won 1.5 your bet!')
            self.amount_of_bet = self.amount_of_bet * 2.5

        elif self.sum_value()[0] > self.sum_value()[-1] or self.sum_value()[-1] > 21:
            print('\nYou won!')
            self.amount_of_bet = self.amount_of_bet * 2

        elif self.sum_value()[0] == self.sum_value()[-1]:
            print('\nIt is a tie')

        else:
            print('\nYou lost')
            self.amount_of_bet = 0
