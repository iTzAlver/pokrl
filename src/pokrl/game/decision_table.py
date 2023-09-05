# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import numpy as np
# Decision table:
# Pair: 1
# Two pairs: 2
# Three of a kind: 3
# Straight: 4
# Flush: 5
# Full house: 6
# Four of a kind: 7
# Straight flush: not implemented as a combination of straight and flush (royal flush is the highest number)
# Game card: decimal number: card number/15


def __check_equal(*cards: tuple[np.ndarray]) -> bool:
    """
    This function checks if the cards are equal.
    :param cards: Cards to check if are equal.
    :return: False if equal, True otherwise.
    """
    for ix, card_0 in enumerate(cards):
        for ox, card_1 in enumerate(cards):
            if np.equal(card_0, card_1).all() and ix != ox:
                return False
    return True


def check_pair(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a pair.
    :param full_hand: Full sorted hand of the player.
    :return: 1 + the card number if there is a pair, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            if card_0[1] == card_1[1] and not np.equal(card_0, card_1).all():
                return 1 + card_0[1] / 15
    return 0.


def check_two_pairs(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains two pairs.
    :param full_hand: Full sorted hand of the player.
    :return: 2 + the card number if there is a two pair, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            for card_2 in full_hand:
                for card_3 in full_hand:
                    if card_0[1] == card_1[1] and card_2[1] == card_3[1] and card_0[1] != card_2[1] \
                            and __check_equal(card_0, card_1, card_2, card_3):
                        return 2 + max(card_0[1], card_2[1]) / 15 + min(card_0[1], card_2[1]) / 150
    return 0.


def check_tok(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a three of a kind.
    :param full_hand: Full sorted hand of the player.
    :return: 3 + the card number if there is a 3ok, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            for card_2 in full_hand:
                if card_0[1] == card_1[1] == card_2[1] and __check_equal(card_0, card_1, card_2):
                    return 3 + card_0[1] / 15
    return 0.


def check_straight(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a straight.
    :param full_hand: Full sorted hand of the player.
    :return: 4 + the card number if there is a straight, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            for card_2 in full_hand:
                for card_3 in full_hand:
                    for card_4 in full_hand:
                        if __check_equal(card_0, card_1, card_2, card_3):
                            if card_0[1] == card_1[1] - 1 == card_2[1] - 2 == card_3[1] - 3 == card_4[1] - 4:
                                return 4 + card_0[1] / 15
                            elif (13 == card_0[1] and 2 == card_1[1] and 3 == card_2[1] and 4 == card_3[1]
                                  and 5 == card_4[1]):
                                return 4.
    return 0.


def check_flush(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a flush.
    :param full_hand: Full sorted hand of the player.
    :return: 5 + the card number if there is a flush, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            for card_2 in full_hand:
                for card_3 in full_hand:
                    for card_4 in full_hand:
                        if card_0[0] == card_1[0] == card_2[0] == card_3[0] == card_4[0] \
                                and __check_equal(card_0, card_1, card_2, card_3, card_4):
                            return 5 + card_0[1] / 15
    return 0.


def check_fh(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a full house.
    :param full_hand: Full sorted hand of the player.
    :return: 6 + the card number if there is a full house, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            for card_2 in full_hand:
                for card_3 in full_hand:
                    for card_4 in full_hand:
                        if __check_equal(card_0, card_1, card_2, card_3, card_4):
                            if card_0[1] == card_1[1] == card_2[1] and card_3[1] == card_4[1]:
                                return 6 + card_0[1] / 15 + card_3[1] / 150
                            elif card_0[1] == card_1[1] and card_2[1] == card_3[1] == card_4[1]:
                                return 6 + card_2[1] / 15 + card_0[1] / 150
    return 0.


def check_fok(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a four of a kind.
    :param full_hand: Full sorted hand of the player.
    :return: 7 + the card number if there is a four of a kind, 0 otherwise.
    """
    for card_0 in full_hand:
        for card_1 in full_hand:
            for card_2 in full_hand:
                for card_3 in full_hand:
                    if (card_0[1] == card_1[1] == card_2[1] == card_3[1] and
                            __check_equal(card_0, card_1, card_2, card_3)):
                        return 7 + card_0[1] / 15
    return 0.


def check_sf(full_hand: np.ndarray) -> float:
    """
    This function checks if the hand contains a straight flush.
    :param full_hand: Full sorted hand of the player.
    :return:
    """
    pf = check_flush(full_hand)
    if pf > 1.:
        return check_straight(full_hand) + 5
    return 0


def get_points(player_hand: np.ndarray, table_hand: np.ndarray):
    """
    This function returns the points of the hand.
    :param player_hand: Hand of the player.
    :param table_hand: Table hand.
    :return: The points of the hand.
    """
    unsorted_full_hand = np.concatenate([player_hand, table_hand])
    full_hand = unsorted_full_hand[np.argsort(unsorted_full_hand[:, 1])[::-1]]
    for check in [check_sf, check_fok, check_fh, check_flush, check_straight, check_tok, check_two_pairs, check_pair]:
        points = check(full_hand)
        if points > 0:
            return points
    return full_hand[0][1] / 15 + full_hand[1][1] / 150

# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
