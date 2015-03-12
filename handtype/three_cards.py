from handtype.base import Base

__author__ = 'avkoltsov'


class ThreeCard(Base):

    def rank(self):
        return 3

    def name(self):
        return 'three cards'

    def exists(self):
        return self.n_of_value(3)

    def value(self):
        return self.highest_more_than(3)