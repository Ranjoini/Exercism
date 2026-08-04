"""Binary search exercise."""

import bisect


def find(search_list, value):
    index = bisect.bisect_left(search_list, value)
    if index != len(search_list) and search_list[index] == value:
        return index
    raise ValueError("value not in array")
