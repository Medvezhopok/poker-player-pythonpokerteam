__author__ = 'Andrew'


class Card:
    RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    SUITS = ('hearts', 'diamonds', 'spades', 'clubs')

    def __init__(self, card_data):
        self.suit = card_data['suit'].lower()
        self.rank = card_data['rank']
        self.value = Card.RANKS.index(self.rank) + 2

    def __hash__(self):
        return self.value

    def __str__(self):
        return '%s of %s' % (self.rank, self.suit)

    def data(self):
        return {
            'rank': Card.RANKS[self.value - 2],
            'suit': self.suit.lower()
        }

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return  self.value <= other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __cmp__(self, other):
        return self.value - other.value