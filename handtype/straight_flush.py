from collections import Counter
from handtype.base import Base

__author__ = 'avkoltsov'


class StraightFlush(Base):

    def rank(self):
        return 8

    def name(self):
        return 'straight flush'

    def value(self):
        suit, count = Counter([card.suit for card in self.cards]).most_common(1)[0]
        if count < 5:
            return False

        cards = [card for card in self.cards if card.suit == suit]
        return self.cards_in_straight(5, cards)

    def exists(self):
        return self.value() > 0
