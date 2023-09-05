# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
# Import statements:
import logging
from pokrl import CoreGame, __version__
logging.basicConfig(level=logging.INFO)
TIME_TO_PLAY = 10  # 10 minutes


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        FUNCTION DEF                       #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
def main() -> None:
    logging.info(f"[+] Connected to test_winners.py v{__version__}")
    # Create a game:
    core_game = CoreGame(number_of_players=9, level_up_each=4, initial_stack=250)
    # Play hands:
    for i in range(10):
        core_game.shuffle_deck()
        hands = core_game.get_cards()
        core_game.flop()
        core_game.turn()
        core_game.river()
        _, points = core_game.get_winner(hands)
        logging.info(f"[+] The winner is: {_}:{points}"
                     f"\nHands: {hands}\nTable: {core_game.table_cards}")
    logging.info(f"[-] Disconnected from test_winners.py v{__version__}")
    return None


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                           MAIN                            #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
if __name__ == '__main__':
    main()
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
