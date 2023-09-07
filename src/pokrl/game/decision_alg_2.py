# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import numpy as np
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
# Define ranks and suits as constants
# Constants for card ranks and suits
RANK_MASK = 0xF  # 4 bits for rank (2 to Ace)
SUIT_MASK = 0xF0  # 4 bits for suit (Spades, Hearts, Diamonds, Clubs)
RANKS = {2: 0x2, 3: 0x3, 4: 0x4, 5: 0x5, 6: 0x6, 7: 0x7, 8: 0x8, 9: 0x9, 10: 0xA, 11: 0xB, 12: 0xC, 13: 0xD, 14: 0xE}
SUITS = {0: 0x10, 1: 0x20, 2: 0x30, 3: 0x40}


def card_to_int(card):
    """
    This function converts a card to an integer.
    :param card: Card to convert.
    :return: The integer of the card.
    """
    rank = RANKS[int(card[1])]
    suit = SUITS[int(card[0])]
    return rank | suit


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
# Function to evaluate a poker hand
def evaluate_poker_hand(full_hand):
    """
    This function evaluates a poker hand.
    :param full_hand: Full sorted hand of the player.
    :return: The points of the hand.
    """
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
    highest_s_rank = 0
    straight_count = 0
    for rank in rank_counts.keys().__reversed__():
        if rank == last_rank + 1:
            straight_count += 1
            if straight_count >= 4:
                highest_s_rank = rank
                is_straight = True
        else:
            straight_count = 0
        last_rank = rank

    if is_flush and is_straight:  # Straight flush [x]
        # Check that all the cards with flush has straight:
        cards_with_flush = list()
        for card in hand_integers:
            if suit_counts[card & SUIT_MASK] >= 5:
                cards_with_flush.append(card & RANK_MASK)
        for card in cards_with_flush:
            if (card + 1 in cards_with_flush and card + 2 in cards_with_flush and card + 3 in
                    cards_with_flush and card + 4 in cards_with_flush):
                return 8. + max(cards_with_flush) / 15
        return 5. + sum([card / (15 * 15 ** i) for i, card in enumerate(cards_with_flush)])

    elif max_count == 4:  # Four of a kind [x]
        # Get the card that its max_count is 4:
        for card in full_hand:
            if rank_counts[card[1]] == 4:
                return 7. + card[1] / 15

    elif max_count == 3 and len(rank_counts) <= 4:  # Full house [x]
        # Get the card that its max_count is 3:
        three_count = 0
        two_count = 0
        for card in full_hand:
            if rank_counts[card[1]] == 3:
                three_count = card[1]
            elif rank_counts[card[1]] == 2:
                two_count = card[1]
        return 6. + three_count / 15 + two_count / 150

    elif is_flush:  # Flush [x]
        # Get the highest card with flush:
        cards_with_flush = list()
        for card in hand_integers:
            if suit_counts[card & SUIT_MASK] >= 5:
                cards_with_flush.append(card & RANK_MASK)
        # Sort the cards with flush:
        cards_with_flush.sort(reverse=True)
        return 5. + sum([card / (15 * 15 ** i) for i, card in enumerate(cards_with_flush)])

    elif is_straight:  # Straight [x]
        # Get the highest card with straight:
        return 4. + highest_s_rank / 15

    elif max_count == 3:  # Three of a kind [x]
        # Get the card that its max_count is 3:
        for card in full_hand:
            if rank_counts[card[1]] == 3:
                return 3. + card[1] / 15 + sum([card / (15 * 15 ** (i + 1)) for i, card in enumerate(full_hand[:, 1])])

    elif max_count == 2 and len(rank_counts) <= 5:  # Two pairs [x]
        # Get the cards that its max_count is 2:
        pairs = list()
        for card in full_hand:
            if rank_counts[card[1]] == 2:
                pairs.append(card[1])
        return (2. + max(pairs) / 15 + min(pairs) / 150 +
                sum([card / (15 * 15 ** (i + 2)) for i, card in enumerate(full_hand[:, 1])]))

    elif max_count == 2:  # Pair [x]
        # Get the card that its max_count is 2:
        for card in full_hand:
            if rank_counts[card[1]] == 2:
                return (1. + card[1] / 15 +
                        sum([card / (15 * 15 ** (i + 1)) for i, card in enumerate(full_hand[:, 1])]))

    else:   # High card [x]
        return sum([card / (15 * 15 ** i) for i, card in enumerate(full_hand[:, 1])])


# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
def get_points_v2(player_hands: np.ndarray, table_hand: np.ndarray):
    """
    This function returns the points of the hand.
    :param player_hands: Hands of the players.
    :param table_hand: Table hand.
    :return: The points of the hand.
    """
    # Get the points of the hands:
    points = list()
    for player_hand in player_hands:
        unsorted_full_hand = np.concatenate([player_hand, table_hand])
        full_hand = unsorted_full_hand[np.argsort(unsorted_full_hand[:, 1])[::-1]]
        points.append(evaluate_poker_hand(full_hand))
    return np.argmax(points), points
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
