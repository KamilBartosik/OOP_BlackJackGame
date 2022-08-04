from cards_values import ranks, suits
from cards import Cards
from random import shuffle


class Deck:

    def __init__(self):

        self.whole_deck = []

        for suit in suits:
            for rank in ranks:
                self.whole_deck.append(Cards(rank, suit))

    def shuffle(self):

        shuffle(self.whole_deck)

    def take_card(self):

        return self.whole_deck.pop(0)

    def __len__(self):

        return len(self.whole_deck)
