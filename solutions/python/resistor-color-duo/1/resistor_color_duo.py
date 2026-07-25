"""Resistor color duo exercise."""

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


def value(colors):
    """Combine the value of the first and second color band."""
    val_one = Colors[colors[0]].value
    val_two = Colors[colors[1]].value
    glued_text = f"{val_one}{val_two}"
    return int(glued_text)
