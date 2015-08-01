from handtype.hand import Hand
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Player:
    VERSION = "Inky 0.1"

    def power(self, hand):
        pass

    def pre_flop_power1(self, hand):
        if hand.rank == 1 and hand.value >= 10:
            return True
        if hand.rank == 0 and hand.value >= 14 and hand.value2 >= 10:
            return True
        return False

    def pre_flop_power3(self, hand):
        if hand.rank == 0 and hand.value <= 7 and hand.value2 >= 2:
            return True
        return False

    def betRequest(self, game_state):
        print pp.pprint(game_state)
        if not 'in_action' in game_state.keys():
            return 0
        self.game_state = game_state
        me = game_state['players'][game_state['in_action']]
        call = game_state['current_buy_in'] - me['bet']
        my_cards = me['hole_cards']
        community_cards = game_state['community_cards']
        pot = game_state['pot']
        blind = game_state['small_blind'] * 2

        rais = game_state['minimum_raise']
        if len(community_cards) == 0:
            # pre flop
            hand = Hand(my_cards)
            if self.pre_flop_power1(hand):
                if call >= blind*3:
                    return call
                else:
                    return blind*3
            if self.pre_flop_power3(hand):
                return 0
            if call < blind * 3:
                return call
            return call
        else:
            cards = my_cards + community_cards
            hand = Hand(cards)
            if hand.rank >= 2:
                return me['stack']
            else:
                return call
        return call

    def showdown(self, game_state):
        pass