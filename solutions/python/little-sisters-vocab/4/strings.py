"""
Module for creating, transforming, and adding prefixes to strings.
Optimized for memory efficiency and robust punctuation handling.
"""

from typing import List


def add_prefix_un(word: str) -> str:
    """Adds the prefix 'un' to a word."""
    return f"un{word}"


def make_word_groups(vocab_words: List[str]) -> str:
    """
    Transforms a list containing a prefix and words into a string
    with the prefix prepended to every subsequent word.
    """
    prefix = vocab_words[0]

    # Use an iterator to step over elements sequentially without duplicating the list via slicing
    word_iterator = iter(vocab_words)
    next(word_iterator)  # Consume and skip the prefix element safely

    # Build the results list directly
    results = [prefix] + [f"{prefix}{word}" for word in word_iterator]
    return " :: ".join(results)


def remove_suffix_ness(word: str) -> str:
    """Removes the suffix 'ness' from a word while handling i->y spelling rules."""
    # Slicing a string is fine here as it's a fixed length (-4 for 'ness')
    root = word[:-4]

    if root.endswith("i"):
        return f"{root[:-1]}y"
    return root


def adjective_to_verb(sentence: str, index: int) -> str:
    """Extracts an adjective from a sentence by index and transforms it into a verb."""
    words = sentence.split()
    adjective = words[index]

    # rstrip targets only trailing punctuation at the end of the word, leaving the front intact
    clean_word = adjective.rstrip('.,!?;"')

    return f"{clean_word}en"
