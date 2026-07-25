"""Raindrops exercise on Exercism."""


def convert(number):
    """Takes an integer and returns Pling/Plang/Plong based on factors."""
    raindrops = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    return "".join(r for f, r in raindrops if number % f == 0) or str(number)
