from handtype.base import Base

__author__ = 'avkoltsov'


class HihgCard(Base):

    def rank(self):
        return 0

    def name(self):
        return 'high card'

    def exists(self):
        return True