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


def score(dice, category):
    SCORING_DICT = {
        YACHT: (lambda d: 50 if len(set(d)) == 1 else 0),
        ONES: lambda d: d.count(1) * 1,
        TWOS: lambda d: d.count(2) * 2,
        THREES: lambda d: d.count(3) * 3,
        FOURS: lambda d: d.count(4) * 4,
        FIVES: lambda d: d.count(5) * 5,
        SIXES: lambda d: d.count(6) * 6,
        FULL_HOUSE: lambda d: sum(d) if sorted(Counter(d).values()) == [2, 3] else 0,
        FOUR_OF_A_KIND: lambda d: next(
            (number * 4 for number in set(d) if d.count(number) >= 4), 0
        ),
        LITTLE_STRAIGHT: lambda d: 30 if sorted(d) == [1, 2, 3, 4, 5] else 0,
        BIG_STRAIGHT: lambda d: 30 if sorted(d) == [2, 3, 4, 5, 6] else 0,
        CHOICE: sum,
    }
    engine = SCORING_DICT.get(category, lambda d: 0)
    return engine(dice)
