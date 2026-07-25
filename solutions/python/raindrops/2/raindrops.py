"""Raindrops exercise on Exercism."""


def convert(number):
    """Takes an integer and returns Pling/Plang/Plong based on factors."""
    raindrops = ""
    if number % 3 == 0:
        raindrops += "Pling"
    if number % 5 == 0:
        raindrops += "Plang"
    if number % 7 == 0:
        raindrops += "Plong"
    return raindrops or str(number)
