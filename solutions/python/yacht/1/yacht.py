# Score categories.
# Change the values as you see fit.
from collections import Counter

YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"


def score(dice: list[int], category) -> int:
    """Map out the actions of each category."""
    if category == YACHT and len(set(dice)) == 1:
        return 50
    elif category == ONES:
        return 1 * dice.count(1)
    elif category == TWOS:
        return 2 * dice.count(2)
    elif category == THREES:
        return 3 * dice.count(3)
    elif category == FOURS:
        return 4 * dice.count(4)
    elif category == FIVES:
        return 5 * dice.count(5)
    elif category == SIXES:
        return 6 * dice.count(6)
    elif category == FULL_HOUSE:
        counts = Counter(dice)
        if sorted(counts.values()) == [2, 3]:
            return sum(dice)
        return 0
    elif category == FOUR_OF_A_KIND:
        for number in set(dice):
            if dice.count(number) >= 4:
                return number * 4
        return 0
    elif (
        category == LITTLE_STRAIGHT
        and sorted(dice) == [1, 2, 3, 4, 5]
        or category == BIG_STRAIGHT
        and sorted(dice) == [2, 3, 4, 5, 6]
    ):
        return 30
    elif category == CHOICE:
        return sum(dice)
    return 0
