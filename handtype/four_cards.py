from handtype.base import Base

__author__ = 'avkoltsov'


class FourCard(Base):

    def rank(self):
        return 7

    def name(self):
        return 'four cards'

    def exists(self):
        return self.n_of_value(4)

    def value(self):
        return self.highest_more_than(4)