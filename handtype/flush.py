from collections import Counter
from handtype.base import Base

__author__ = 'avkoltsov'


class Flush(Base):

    def rank(self):
        return 5

    def name(self):
        return 'flush'

    def exists(self):
        suit, count = Counter([card.suit for card in self.cards]).most_common(1)[0]
        if count >= 5:
            return True
        return False