from collections.abc import Callable
from typing import Any


def append(list1: list, list2: list) -> list:
    return list1 + list2


def concat(lists: list) -> list:
    flat_list = []
    for inner_list in lists:
        flat_list.extend(inner_list)
    return flat_list


def filter(function: Callable, lst: list) -> list:
    return [item for item in lst if function(item)]


def length(lst: list) -> int:
    return len(lst)


def map(function: Callable, lst: list) -> list:
    return [function(item) for item in lst]


def foldl(function: Callable, lst: list, initial: Any) -> Any:
    accumulator = initial
    for item in lst:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function: Callable, lst: list, initial: Any) -> Any:
    accumulator = initial
    for item in lst[::-1]:
        accumulator = function(accumulator, item)
    return accumulator


def reverse(lst: list) -> list:
    return lst[::-1]
