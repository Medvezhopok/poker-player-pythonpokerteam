from handtype.hand import Hand
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Player:
    VERSION = "Inky 0.1"

    def betRequest(self, game_state):
        print pp.pprint(game_state)
        if not 'in_action' in game_state.keys():
            return 0

        me = game_state['players'][game_state['in_action']]
        call = game_state['current_buy_in'] - me['bet']
        my_cards = me['hole_cards']
        community_cards = game_state['community_cards']
        if len(community_cards) == 0:
            # pre flop
            hand = Hand(my_cards)
            if hand.rank > 1:
                return me['stack']
            if hand.rank == 1:

            pass
        else:
            cards = my_cards + community_cards
            pass


        return me['stack']

    def showdown(self, game_state):
        pass