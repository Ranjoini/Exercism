"""Darts exercise."""

import math


def score(x: float, y: float) -> int:
    """Determine the points scored using the coordinates."""
    distance = math.hypot(x, y)
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0
