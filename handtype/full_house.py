from collections import Counter
from handtype.base import Base

__author__ = 'avkoltsov'


class FullHouse(Base):

    def rank(self):
        return 6

    def name(self):
        return 'full house'

    def exists(self):
        return self.n_of_value(3) and (self.value2() > 0)

    def value(self):
        return self.highest_more_than(3)

    def value2(self):
        return self.highest_more_than(2, self.value())