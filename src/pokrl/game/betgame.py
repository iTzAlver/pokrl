# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
"""
File info:
"""
# Import statements:
import numpy as np
from .pokgame import CoreGame
from ..__special__ import __version__


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        MAIN CLASS                         #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
class PokerGame:
    def __init__(self, number_of_players: int = 9, level_up_each: int = 4, initial_stack: int = 100,
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
        The scope is defined as all the visible actions and cards of the player.
        Scope elements:

        - Card scope:
        [0]: Player card 1 range (2-14) normalized to 0-1.
        [1-4]: Player card 1 color (0-3) one-hot encoded.
        [5]: Player card 2 range (2-14) normalized to 0-1.
        [6-9]: Player card 2 color (0-3) one-hot encoded.

        - Position scope:
        [10]: Distance from Hero to Big Blind (0-8) normalized to 0-1; 0 is UTG1 and 1 is BB.
        [11]: Villain 1 action (0-1) 0 means fold, 1 means all-in, relative to their stack. ( SB )
        [12]: Villain 2 action (0-1) 0 means fold, 1 means all-in, relative to their stack. ( BB )
        [13]: Villain 3 action (0-1) 0 means fold, 1 means all-in, relative to their stack. (UTG1)
        [14]: Villain 4 action (0-1) 0 means fold, 1 means all-in, relative to their stack. (UTG2)
        [15]: Villain 5 action (0-1) 0 means fold, 1 means all-in, relative to their stack. ( LJ )
        [16]: Villain 6 action (0-1) 0 means fold, 1 means all-in, relative to their stack. ( HJ )
        [17]: Villain 7 action (0-1) 0 means fold, 1 means all-in, relative to their stack. ( CO )
        [18]: Villain 8 action (0-1) 0 means fold, 1 means all-in, relative to their stack. (BTN )

        - Random scope (for frequency actions):
        [19]: A random number between 0 and 1.

        - Stack scope:
        [20]: Hero stack (0-1) normalized to 0-1 from all to his part.
        [21]: Villain 1 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [22]: Villain 2 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [23]: Villain 3 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [24]: Villain 4 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [25]: Villain 5 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [26]: Villain 6 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [27]: Villain 7 stack (0-1) normalized to 0-1 from 0 to all the pot.
        [28]: Villain 8 stack (0-1) normalized to 0-1 from 0 to all the pot.

        - Current pot scope:
        [29]: Pot (0-1) normalized to 0-1 from 0 to all the pot.
        [30]: Flop card 1 range (2-14) normalized to 0-1.
        [31-34]: Flop  card 1 color (0-3) one-hot encoded.
        [35]: Flop  card 2 range (2-14) normalized to 0-1.
        [36-39]: Flop card 2 color (0-3) one-hot encoded.
        [40]: Flop  card 3 range (2-14) normalized to 0-1.
        [41-44]: Flop  card 3 color (0-3) one-hot encoded.
        [45]: Turn card range (2-14) normalized to 0-1.
        [46-49]: Turn card color (0-3) one-hot encoded.
        [50]: River card range (2-14) normalized to 0-1.
        [51-54]: River card color (0-3) one-hot encoded.

        - State scope:
        [55]: Current game state. 0: Pre-flop, 0.25: Flop, 0.5: Turn, 0.75: River, 1: Showdown.

        self.scopes[encoding, player]

        Actions: -1 fold, 0 check/call, >0. bet/raise.
        """
        self.__version__ = __version__

        # Initialize the scopes:
        initial_scopes = np.zeros((56, 9), np.float32)
        initial_scopes[19, :] = np.random.random(9)
        initial_scopes[20:28, :] = 1 / 9 * np.ones(9)
        self.scopes = initial_scopes

        # Initialize the game:
        self.core = CoreGame(number_of_players, game_seed)
        self.hand_number = 0
        self.level_up_each = level_up_each
        self.initial_stack = initial_stack
        self.level_table = level_table
        self.current_level_table = level_table[0]

        # Initialize the players:
        self.hands = np.array([])
        self.model = None

    def play_round(self):
        """
        This method plays a round of the game.
        :return: None
        """
        # Shuffle the deck:
        self.core.shuffle_deck()

        # Start the game:
        self.hands = self.core.get_cards()
        self.scopes[0:2, :] = self.hands[:, 0, :]

        # Ask pre-flop:
        self.hand_number += 1
        if (self.hand_number % self.level_up_each == 0 and
                (level := self.hand_number // self.level_up_each) < self.level_table.shape[0]):
            self.current_level_table = self.level_table[level, :]
            self.scopes[55, :] = 0

    def ask_players(self) -> np.ndarray:
        """
        Ask the players their actions based on the current scope.
        :return: Each player actions.
        """
        round_scope = self.scopes.copy()
        player_actions = np.zeros((9,), np.float32)
        for pn in range(9):
            player_scope = round_scope[:, pn]
            action = self.model.predict(player_scope)
            player_actions[pn] = action
            round_scope[11 + pn, :] = action
        self.scopes = round_scope
        return player_actions


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
