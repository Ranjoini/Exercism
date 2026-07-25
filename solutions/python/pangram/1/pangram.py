"""Pangram exercise."""

import string


def is_pangram(sentence: str) -> bool:
    """Check if pangram."""
    clean_sentence = sentence.lower()
    for letter in string.ascii_lowercase:
        if letter not in clean_sentence:
            return False

    return True
