"""Resistor color exercise."""

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


def color_code(color):
    """Look up the numerical value associated with a particular color band."""
    return Colors[color].value


def colors():
    """List the different bands of colors."""
    return list(Colors.__members__.keys())
