# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import numpy as np
from ..__special__ import __version__
from .decision_table import get_points
from .decision_alg_2 import get_points_v2


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
class CoreGame:
    def __init__(self, number_of_players: int = 9, level_up_each: int = 4, initial_stack: int = 250,
                 level_table: np.ndarray = np.array([]), game_seed: int = None):
        """
        The CoreGame class is the main class of the game. It contains the main logic of the game. The game is
        parametrized by 4 parameters [3 int, 1 matrix]:

        This class creates the deck attribute, (color [0, 1, 2, 3] , card number [1-12])
        The deck is randomly shuffled at its initial state.
        The stack is normalized to Big Blinds (BBs).

        :param number_of_players: Number of maximum players allowed in the game.
        :param level_up_each: Number of hands to play before the blinds level up.
        :param initial_stack: Initial stack for each player.
        :param level_table: Table of blinds and antes for each level. [level] -> [small_blind, big_blind, ante]
        :param game_seed: Seed for the game.
        """
        # Game main parameters:
        self.__version__ = __version__
        self.number_of_players = number_of_players
        self.level_up_each = level_up_each
        self.initial_stack = initial_stack
        self.level_up_table = level_table
        self.__game_seed = game_seed
        # Game state parameters:
        self.current_level = 0
        self.deck_pointer = 0
        self.table_cards = np.array([])
        # + Create an array with 52 cards (from 2 to 14 and from 1 to 4):
        self.__deck = np.reshape(np.array([[(j, i) for i in range(2, 15)] for j in range(4)], dtype=np.int8),
                                 (-1, 2))
        self.deck = None
        np.random.seed(self.__game_seed)
        self.shuffle_deck()

    def shuffle_deck(self):
        """
        This method shuffles the deck.
        :return: None
        """
        _deck = self.__deck.copy()
        np.random.shuffle(_deck)
        self.deck = _deck
        self.deck_pointer = 0

    def get_cards(self, number_of_current_players: int = 0):
        """
        This method returns a list of 2 cards from the deck for all players.
        :param number_of_current_players: Number of players to deal cards.
        :return: List of 2 cards from the deck for each active player.
        """
        # Get the number of cards to deal:
        number_of_current_players = self.number_of_players if number_of_current_players == 0 \
            else number_of_current_players
        hand_cards = self.deck[0:number_of_current_players * 2]
        hands = np.concatenate([hand_cards[0::2], hand_cards[1::2]], axis=1)
        hands = np.reshape(hands, (number_of_current_players, 2, 2))
        # Update deck pointer.
        self.deck_pointer += number_of_current_players * 2
        return hands

    def flop(self):
        # Burn a card.
        self.deck_pointer += 1
        # Get the flop cards.
        flop_cards = self.deck[self.deck_pointer:self.deck_pointer + 3]
        self.deck_pointer += 3
        # Extend table cards:
        self.table_cards = flop_cards
        return flop_cards

    def turn(self):
        # Burn a card.
        self.deck_pointer += 1
        # Get the flop cards.
        turn_card = self.deck[self.deck_pointer]
        self.deck_pointer += 1
        # Extend table cards:
        self.table_cards = np.concatenate([self.table_cards, [turn_card]])
        return turn_card

    def river(self):
        # Burn a card.
        self.deck_pointer += 1
        # Get the flop cards.
        river_card = self.deck[self.deck_pointer]
        self.deck_pointer += 1
        # Extend table cards:
        self.table_cards = np.concatenate([self.table_cards, [river_card]])
        return river_card

    def get_winner(self, hands: np.ndarray = np.array([])):
        """
        This method returns the winner of the game.
        :param hands: List of hands to compare.
        :return: Winner of the game.
        """
        # Get the points of the hand:
        winner, points = get_points_v2(hands, self.table_cards)
        return winner, points

    def __repr__(self):
        return f'CoreGame class instance v{self.__version__}'
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
