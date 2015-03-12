from handtype.base import Base

__author__ = 'avkoltsov'


class Pair(Base):

    def rank(self):
        return 1

    def name(self):
        return 'pair'

    def exists(self):
        return self.n_of_value(2)

    def value(self):
        return self.highest_more_than(2)