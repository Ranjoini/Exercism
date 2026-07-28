"""Resistor color trio."""

import enum


class Colors(enum.IntEnum):
    black = 0
    brown = 1
    red = 2
    orange = 3
    yellow = 4
    green = 5
    blue = 6
    violet = 7
    grey = 8
    white = 9


def label(colors):
    """Label the resistor based on the colors given."""
    # Find the values of the color band
    val_one = Colors[colors[0]].value
    val_two = Colors[colors[1]].value
    val_three = 10 ** Colors[colors[2]].value
    # Calculate the totol resistance
    total_ohms = ((val_one * 10) + val_two) * val_three
    # prefixes and tracker for the current index to determine the prefix to be used
    prefixes = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    prefix_index = 0
    while 0 < total_ohms and total_ohms % 1000 == 0:
        total_ohms //= 1000
        prefix_index += 1
    # format the final result
    return f"{total_ohms} {prefixes[prefix_index]}"
