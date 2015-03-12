from collections import Counter

__author__ = 'Andrew'


class Base:

    def __init__(self, cards):
        self.cards = cards

    def exists(self):
        return False

    def value(self):
        return self.cards[-1].value

    def value2(self):
        return self.value()

    def __str__(self):
        return self.name()

    def name(self):
        return 'unknown'

    def second_value(self):
        return self.value()

    def n_of_value(self, n):
        return self.highest_more_than(n) > 0

    def highest_more_than(self, n, exept_value=None):
        exept_value = exept_value or 0
        counter = Counter([card.value for card in self.cards if card.value != exept_value])
        most_common = counter.most_common()
        for common in most_common:
            value, count = common
            if count >= n:
                return value

        return 0

    def cards_in_straight(self, n, cards):
        counter = Counter([card.value for card in cards])
        for card in cards:
            if card.rank == 'A':
                counter[1] += 1

        common = counter.most_common()
        common.sort(lambda x, y: x[0] - y[0])

        count = 1
        last_value, _ = common[0]
        for card_value, _ in common[1:]:
            if card_value - last_value != 1:
                count = 1
            else:
                count += 1
            last_value = card_value

            if count >= n:
                return last_value

        return 0
