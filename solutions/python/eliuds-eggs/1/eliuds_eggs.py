"""Eliud's eggs."""


def egg_count(display_value):
    """Convert the number of eggs show in the display value to the actual number of eggs in the coup."""
    total_egg_count = 0
    while display_value > 0:
        total_egg_count += display_value & 1
        display_value >>= 1
    return total_egg_count
