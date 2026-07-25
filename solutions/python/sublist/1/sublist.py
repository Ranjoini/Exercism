"""Sublist exercise."""

from typing import Any


SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def contains(big_list: list[Any], small_list: list[Any]) -> bool:
    """Checks if small_list is a contiguous sequence inside big_list."""

    if not small_list:
        return True
    for i in range(len(big_list) - len(small_list) + 1):
        if big_list[i : i + len(small_list)] == small_list:
            return True
    return False


def sublist(list_one: list[Any], list_two: list[Any]) -> int:
    """Determines the structural relationship between two lists."""
    if list_one == list_two:
        return EQUAL
    elif contains(list_one, list_two):
        return SUPERLIST
    elif contains(list_two, list_one):
        return SUBLIST
    else:
        return UNEQUAL
