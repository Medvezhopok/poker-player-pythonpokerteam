from handtype.hand import Hand
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Player:
    VERSION = "Inky 0.10"

    def pre_flop_power1(self, hand):
        print 'check for power hand for %s' % hand
        if hand.rank > 1:
            return True
        if hand.rank == 1 and hand.value >= 11:
            return True
        if hand.rank == 0 and hand.value > 13 and hand.value2 >= 11:
            return True
        return False

    def pre_flop_power3(self, hand):
        if hand.rank == 0 and hand.value <= 7:
            return True
        return False

    def betRequest(self, game_state):
        try:
            if not 'in_action' in game_state.keys():
                return 0
            active_players = []
            for p in game_state['players']:
                if 'active' == p['status']:
                    active_players.append(p['name'])

            self.game_state = game_state
            me = game_state['players'][game_state['in_action']]
            call = game_state['current_buy_in'] - me['bet']
            my_cards = me['hole_cards']
            community_cards = game_state['community_cards'] or []
            pot = game_state['pot']
            blind = game_state['small_blind'] * 2
            bet_index = game_state['bet_index']
            rais = game_state['minimum_raise']
            hand = Hand(my_cards + community_cards)
            print "HAND %s" % hand

            if len(active_players) > 2:
                if not self.pre_flop_power3(hand):
                    if hand.rank == 2:
                        return call + rais
                    if hand.rank == 1 and hand.value > 11:
                        return call + rais
                    if call > 80:
                        return 0
                    else:
                        return call
                else:
                    return 0
            else:
                if self.pre_flop_power1(hand):
                    return call + 2 * rais
                if self.pre_flop_power3(hand):
                    return 0
                if call > 150:
                    return 0
                else:
                    return call

        except Exception as e:
            print e
        return 0

    def showdown(self, game_state):
        pass
