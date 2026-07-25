"""
Module for tracking card dealer analytics and round combinations.
Optimized using advanced list slicing step configurations.
"""

from typing import List

JACK: int = 11


def get_rounds(number: int) -> List[int]:
    """Generates a list containing the current and next two round numbers."""
    return list(range(number, number + 3))


def concatenate_rounds(rounds_1: List[int], rounds_2: List[int]) -> List[int]:
    """Combines two lists of round numbers via standard concatenation."""
    return rounds_1 + rounds_2


def list_contains_round(rounds: List[int], number: int) -> bool:
    """Verifies existence of a target round inside a sequence of numbers."""
    return number in rounds


def card_average(hand: List[int]) -> float:
    """Computes the exact mathematical mean value of cards in a hand."""
    # Guard against zero-division errors if an empty hand is processed
    return sum(hand) / len(hand) if hand else 0.0


def approx_average_is_average(hand: List[int]) -> bool:
    """Validates if calculated mean matches alternative quick-averaging heuristics."""
    if not hand:
        return False

    calculated_average = card_average(hand)
    first_last_avg = (hand[0] + hand[-1]) / 2
    middle_card = hand[len(hand) // 2]

    return calculated_average in (first_last_avg, middle_card)


def average_even_is_average_odd(hand: List[int]) -> bool:
    """Checks if the mean of even-indexed cards equals the mean of odd-indexed cards."""
    # Slicing syntax -> [start:stop:step]
    even_cards = hand[::2]  # Starts at 0, grabs every 2nd element
    odd_cards = hand[1::2]  # Starts at 1, grabs every 2nd element

    return card_average(even_cards) == card_average(odd_cards)


def maybe_double_last(hand: List[int]) -> List[int]:
    """Mutates the last element to double its value if it matches a Jack."""
    if hand and hand[-1] == JACK:
        hand[-1] = JACK * 2
    return hand
