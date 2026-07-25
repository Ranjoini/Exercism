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
    len_one = len(list_one)
    len_two = len(list_two)
    if len_one < len_two:
        if contains(big_list=list_two, small_list=list_one):
            return SUBLIST
    elif len_one > len_two:
        if contains(big_list=list_one, small_list=list_two):
            return SUPERLIST
    return UNEQUAL
