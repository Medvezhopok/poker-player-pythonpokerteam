from handtype.base import Base

__author__ = 'avkoltsov'


class Straight(Base):

    def rank(self):
        return 4

    def name(self):
        return 'straight'

    def exists(self):
        return self.value() > 0

    def value(self):
        return self.cards_in_straight(5, self.cards)