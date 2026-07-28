"""Resistor color expert."""

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


TOLERANCE = {
    "grey": "0.05%",
    "violet": "0.1%",
    "blue": "0.25%",
    "green": "0.5%",
    "brown": "1%",
    "red": "2%",
    "gold": "5%",
    "silver": "10%",
}


def resistor_label(colors):
    """Use indexing to seclude the last two values and the fisrt values."""
    if len(colors) == 1:
        return "0 ohms"
    # Used slicing to get the multiplier and the tolerance values
    tolreance_str = TOLERANCE[colors[-1]]
    multiplier = 10 ** Colors[colors[-2]].value
    # Getting the value of everything before the last tow values
    digit_str = "".join(str(Colors[c].value) for c in colors[:-2])
    total_ohms = int(digit_str) * multiplier
    # Used the metrics I formed in a former exercise
    prefixes = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    prefix_index = 0
    while total_ohms >= 1000:
        total_ohms /= 1000
        prefix_index += 1
    if total_ohms == int(total_ohms):
        total_ohms = int(total_ohms)

    # Format and return with tolerance added
    return f"{total_ohms} {prefixes[prefix_index]} ±{tolreance_str}"
