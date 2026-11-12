from collections import Counter

RANK_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def evaluate_hand(hand_str):
    # Making the data
    cards = hand_str.split()
    suits = [card[-1] for card in cards]
    # Slicing solves the issue of cards such us 10C
    ranks = [RANK_VALUES[card[:-1]] for card in cards]

    # Count the frequencies and generate the fingerprint
    counts = Counter(ranks)
    fingerprint = sorted(counts.values(), reverse=True)

    # Sort the cards by (Frequency, rank) to help in tie-breaking
    ordered_ranks = sorted(counts.keys(), key=lambda r: (counts[r], r), reverse=True)

    # Flushes and straights
    is_flush = len(set(suits)) == 1
    is_straight = (ordered_ranks[0] - ordered_ranks[-1] == 4) and fingerprint == [
        1,
        1,
        1,
        1,
        1,
    ]

    # The A edge case
    if ordered_ranks == [14, 5, 4, 3, 2]:
        is_straight = True
        ordered_ranks = [5, 4, 3, 2, 1]

    # Scoring engine
    if fingerprint == [1, 1, 1, 1, 1]:
        if is_flush and is_straight:
            score = 8
        elif is_flush:
            score = 5
        elif is_straight:
            score = 4
        else:
            score = 0
    elif fingerprint == [4, 1]:
        score = 7
    elif fingerprint == [3, 2]:
        score = 6
    elif fingerprint == [3, 1, 1]:
        score = 3
    elif fingerprint == [2, 2, 1]:
        score = 2
    # Don't need to check the last score fingerprint, plus it satisfies the linter when you end with else
    else:
        score = 1

    # Construct into a tuple
    return (score, ordered_ranks)


def best_hands(hands):
    # Find the winning hand
    winning_tuple = max(evaluate_hand(hand) for hand in hands)
    # We can have two winners so that's why we are looking for any other similar hand in the hands
    return [hand for hand in hands if evaluate_hand(hand) == winning_tuple]
