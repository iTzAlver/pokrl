# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import numpy as np
# Constants for card ranks and suits
RANK_MASK = 0xF  # 4 bits for rank (2 to Ace)
SUIT_MASK = 0xF0  # 4 bits for suit (Spades, Hearts, Diamonds, Clubs)

# Define ranks and suits as constants
RANKS = {2: 0x2, 3: 0x3, 4: 0x4, 5: 0x5, 6: 0x6, 7: 0x7, 8: 0x8, 9: 0x9, 10: 0xA, 11: 0xB, 12: 0xC, 13: 0xD, 14: 0xE}
SUITS = {0: 0x10, 1: 0x20, 2: 0x30, 3: 0x40}


def card_to_int(card):
    rank = RANKS[int(card[1])]
    suit = SUITS[int(card[0])]
    return rank | suit


# Function to evaluate a poker hand
def evaluate_poker_hand(full_hand):
    # Convert hand to a list of integers
    hand_integers = [card_to_int(card) for card in full_hand]

    # Compute the counts and rank counts:
    rank_counts = {}
    suit_counts = {}
    for card in hand_integers:
        rank = card & RANK_MASK
        suit = card & SUIT_MASK
        if rank in rank_counts:
            rank_counts[rank] += 1
        else:
            rank_counts[rank] = 1
        if suit in suit_counts:
            suit_counts[suit] += 1
        else:
            suit_counts[suit] = 1
    max_count = max(rank_counts.values())

    # Check for specific poker hand combinations
    is_flush = max(suit_counts.values()) >= 5
    is_straight = False
    last_rank = 1 if 14 in rank_counts else 0
    straight_count = 0
    for rank in rank_counts.keys().__reversed__():
        if rank == last_rank + 1:
            straight_count += 1
            if straight_count >= 4:
                is_straight = True
        else:
            straight_count = 0
        last_rank = rank

    if is_flush and is_straight:
        return 8. + full_hand[0][1] / 15
    elif max_count == 4:
        return 7. + full_hand[0][1] / 15
    elif max_count == 3 and len(rank_counts) <= 4:
        return 6.
    elif is_flush:
        return 5. + full_hand[0][1] / 15
    elif is_straight:
        return 4. + full_hand[0][1] / 15
    elif max_count == 3:
        return 3.
    elif max_count == 2 and len(rank_counts) <= 5:
        return 2.
    elif max_count == 2:
        return 1.
    else:
        return sum([card / (15 * 10 ** i) for i, card in enumerate(full_hand[:, 1])])


def get_points_v2(player_hand: np.ndarray, table_hand: np.ndarray):
    """
    This function returns the points of the hand.
    :param player_hand: Hand of the player.
    :param table_hand: Table hand.
    :return: The points of the hand.
    """
    unsorted_full_hand = np.concatenate([player_hand, table_hand])
    full_hand = unsorted_full_hand[np.argsort(unsorted_full_hand[:, 1])[::-1]]
    return evaluate_poker_hand(full_hand)
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
