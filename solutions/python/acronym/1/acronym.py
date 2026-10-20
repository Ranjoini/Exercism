"""Acronym exercise."""

import string


def abbreviate(words: str) -> str:
    """Clean the sentence of any punctation, split the words, capitalize the first letters and return as a string."""
    punctuation = string.punctuation.replace("'", "")
    # Used a dict instead of having to match every single punctuation with a space using " " * len(punctuation)
    punct_dict = {char: " " for char in punctuation}
    translation_table = str.maketrans(punct_dict)
    clean_sentence = words.translate(translation_table)
    acronym = [word[:1].upper() for word in clean_sentence.split()]
    return "".join(acronym)
