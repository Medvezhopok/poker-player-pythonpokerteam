from collections import Counter
import random
from handtype.card import Card
from handtype.hand import Hand
import pprint

pp = pprint.PrettyPrinter(indent=4)

class Player:
    VERSION = "Inky 0.8"

    def cardsInLine(self, a_cards):
        cards = [Card(card) for card in a_cards]
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
        return count

    def isOneVsOne(self):
        active = 0
        names = []
        for p in self.game_state['players']:
            if p['status'] == 'active':
                active += 1
                names.append(p['name'])
        if active == 2:
            return True, names
        return False, []

    def power(self, hand):
        pass

    def pre_flop_power1(self, hand):
        print 'check for power hand for %s' % hand
        if hand.rank == 1 and hand.value >= 10:
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
                print("QQQ, %d, %s, %s" % (game_state['round'], p['name'], p['status']))
                if 'active' == p['status']:
                    active_players.append(p['name'])

            self.game_state = game_state
            me = game_state['players'][game_state['in_action']]
            call = game_state['current_buy_in'] - me['bet']
            my_cards = me['hole_cards']
            community_cards = game_state['community_cards']
            pot = game_state['pot']
            blind = game_state['small_blind'] * 2
            bet_index = game_state['bet_index']
            rais = game_state['minimum_raise']
            hand = Hand(my_cards)
            print "HAND %s" % hand

            if len(active_players) > 2:
                if len(community_cards) == 0:
                    if self.pre_flop_power1(hand):
                        if random.random() > 0.5:
                            return call + rais
                        else:
                            return me['stack']
                    else:
                        if call > 40:
                            return 0
                        else:
                            return call
                else:
                    if hand.rank > 2:
                        return call + rais
                    # if hand.rank == 1 and hand.value > 7:
                    #     return me['stack']
                    # if hand.rank == 0 and hand.value > 10:
                    #     return call
                    return 0

            isOneVsOne, names = self.isOneVsOne()
            if isOneVsOne and 'PythonPokerTeam' in names:
                if hand.rank > 1:
                    return call + rais
                print 'one on one'
                names.remove('PythonPokerTeam')
                enemy_name = names[0]
                print 'enemy_name=%s' % enemy_name
                enemy_player = None
                for player in game_state['players']:
                    if player['name'] == enemy_player:
                        enemy_player = player
                if enemy_player:
                    if enemy_name == 'sevenbits':
                        if not self.pre_flop_power1(hand):
                            return 0
                        if community_cards and enemy_player['bet'] > 0:
                            return 0
                        if enemy_player['stack'] < rais * 5:
                            return enemy_player['stack']
                        return call + rais
                    if enemy_name == 'Awesome Incredible Poker Bot':
                        return call + rais
                    if enemy_name == 'LeanNodeJS':
                        if hand.rank == 1 and enemy_player:
                            if enemy_player['stack'] <= 4 * rais:
                                return me['stack']
                            return call + rais
                    if enemy_name == 'Boris' or enemy_name == 'JBot':
                        return call + 2 * rais

            if len(community_cards) == 0:
                print 'cards_str:'
                cards_str = []
                for c in my_cards:
                    cards_str.append(str(c))
                print cards_str
                # pre flop
                # power hand
                if self.pre_flop_power1(hand):
                    print 'power'
                    if call >= blind*3:
                        return call
                    else:
                        return call + 2*rais

                # save money
                if me['stack'] < 368:
                    print 'saving money'
                    return 0

                active = 0
                for p in self.game_state['players']:
                    if p['status'] == 'active':
                        active += 1

                # weak hand
                if self.pre_flop_power3(hand):
                    print 'pass'
                    return 0
                print 'middle'

                suit, count = Counter([card['suit'] for card in my_cards]).most_common(1)[0]
                if count == 2:
                    return call

                if call <= blind * 3 and bet_index < 1:
                    return call
                if bet_index >= 1 and 3 * me['bet'] <= call:
                    return 0
                elif bet_index >= 1:
                    return call

                return 0

            else:
                print 'board_str:'
                cards = my_cards + community_cards
                board_str = []
                for c in community_cards:
                    board_str.append(str(c))
                print board_str
                hand = Hand(cards)
                print "HAND %s" % hand
                if hand.rank >= 2:
                    return call + 2 * rais

                suit, count = Counter([card['suit'] for card in cards]).most_common(1)[0]
                if len(cards) == 5 and count == 4:
                    return call + rais
                if len(cards) == 6 and count == 4:
                    return call

                if len(cards) == 5 and self.cardsInLine(cards) == 4:
                    return call + rais
                if len(cards) == 6 and self.cardsInLine(cards) == 4:
                    return call

                if hand.rank == 1 and hand.value >= 10:
                    return call + rais

                if hand.rank == 0 and hand.value == 14:
                    return call

                if hand.rank == 0 and hand.value < 6:
                    return 0
            return call
        except Exception as e:
            print e
        return 0

    def showdown(self, game_state):
        pass
