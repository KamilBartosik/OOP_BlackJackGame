from cards_values import values


class Cards:

    # Makes cards as objects and uses them in Deck class

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'
