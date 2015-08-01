from holdem import holdem_functions
from holdem.holdem_argparser import parse_hole_cards

__author__ = 'Andrew'

hand_str = ["Ad", "Kd"]
board_str = ["2h", "3h", "4h"]
hole_cards = parse_hole_cards(hand_str)
board = parse_hole_cards(board_str)

all_cards = list(hole_cards)
all_cards.append(board)
deck = holdem_functions.generate_deck(hole_cards+board)
