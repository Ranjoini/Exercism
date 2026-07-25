"""
Module for scoring and evaluating blackjack hands.
Optimized with data-map lookups and consistent type definitions.
"""

from typing import Tuple, Union

# Define a global look-up map for card values to keep code clean and maintainable
CARD_VALUES = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 1,
}


def value_of_card(card: str) -> int:
    """Returns the point value of a card string using our global map."""
    return CARD_VALUES[card]


def higher_card(card_one: str, card_two: str) -> Union[str, Tuple[str, str]]:
    """
    Determine which card has a higher value.
    Explicitly typed to handle both string or tuple returns safely.
    """
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if v1 > v2:
        return card_one
    if v2 > v1:
        return card_two
    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Calculate whether the ace should be valued at 1 or 11 points."""
    # If the hand already contains an Ace, any subsequent Ace must be valued at 1
    if card_one == "A" or card_two == "A":
        return 1

    total_points = value_of_card(card_one) + value_of_card(card_two)
    return 11 if total_points + 11 <= 21 else 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Determine if the hand forms a natural 21 (Blackjack)."""
    # A natural blackjack must contain exactly one Ace and one 10-value card
    has_ace = card_one == "A" or card_two == "A"
    has_ten = value_of_card(card_one) == 10 or value_of_card(card_two) == 10

    # Ensure it's not a pair of Aces or two tens
    return has_ace and has_ten and card_one != card_two


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Determine if a player can split their hand into two separate hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Determine if a blackjack player can place a double down bet (totaling 9, 10, or 11)."""
    return value_of_card(card_one) + value_of_card(card_two) in {9, 10, 11}
