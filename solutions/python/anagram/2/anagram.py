"""Anagram exercise."""

from collections import Counter


def find_anagrams(word, candidates):
    """Check the list for anagrams and return them in a list."""
    target_count = Counter(word.lower())
    return [
        c
        for c in candidates
        if c.lower() != word.lower() and Counter(c.lower()) == target_count
    ]
