# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
# Import statements:
import logging
import time
from pokrl import CoreGame, __version__
logging.basicConfig(level=logging.INFO)


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        FUNCTION DEF                       #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
def main() -> None:
    logging.info(f"[+] Connected to test_perf.py v{__version__}")
    # Create a game:
    core_game = CoreGame(number_of_players=9, level_up_each=4, initial_stack=250)
    # Play hands:
    ts_zero = time.perf_counter()
    ts_curr = ts_zero
    number_of_games = 0
    while ts_curr - ts_zero < 60 * 3:
        for i in range(1000):
            core_game.shuffle_deck()
            core_game.get_cards()
            core_game.flop()
            core_game.turn()
            core_game.river()
            core_game.get_winner()
        number_of_games += 1000
        ts_curr = time.perf_counter()
    ts_end = time.perf_counter()
    logging.info(f"[!] The current game is played at {number_of_games / (ts_end - ts_zero)} games per second (gps).")
    logging.info(f"[-] Disconnected from test_perf.py v{__version__}")
    return None


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                           MAIN                            #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
if __name__ == '__main__':
    main()
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
