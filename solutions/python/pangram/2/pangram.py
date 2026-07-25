"""Pangram exercise."""

import string


def is_pangram(sentence: str) -> bool:
    """Check if pangram."""
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))
