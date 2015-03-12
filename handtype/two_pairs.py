from collections import Counter
from handtype.base import Base

__author__ = 'avkoltsov'


class TwoPairs(Base):

    def rank(self):
        return 2

    def name(self):
        return 'two pairs'

    def exists(self):
        if len(self.cards) < 5:
            return False
        counter = Counter([card.value for card in self.cards])
        most_common2 = counter.most_common(2)[1]
        value, count = most_common2
        if count >= 2:
            return True
        return False

    def value(self):
        return self.highest_more_than(2)

    def value2(self):
        return self.highest_more_than(2, self.value())