from card import Card
from handtype.flush import Flush
from handtype.four_cards import FourCard
from handtype.full_house import FullHouse
from handtype.high_card import HihgCard
from handtype.pair import Pair
from handtype.straight import Straight
from handtype.straight_flush import StraightFlush
from handtype.three_cards import ThreeCard
from handtype.two_pairs import TwoPairs

__author__ = 'avkoltsov'

HAND_TYPES = [StraightFlush, FourCard, FullHouse, Flush, Straight, ThreeCard, TwoPairs, Pair, HihgCard]


class Hand:

    def __init__(self, cards):
        cards.sort()

        self.cards = [Card(card) for card in cards]
        self.rank = -1
        self.value = 0
        self.value2 = 0
        data = self.calc_rank()
        if data:
            self.rank = data.rank()
            self.value = data.value()
            self.value2 = data.value2()

    def __str__(self):
        return "hank=%s;value=%s;value2=%s" % (self.rank, self.value, self.value2)

    def __cmp__(self, other):
        if self.rank != other.rank:
            return cmp(self.rank, other.rank)
        if self.value != other.value:
            return cmp(self.value, other.value)
        if self.value2 != other.value2:
            return cmp(self.value2, other.value2)

    def calc_rank(self):
        pass
        for hand_type_class in HAND_TYPES:
            hand_type = hand_type_class(self.cards)
            if hand_type.exists():
                return hand_type
        return None
