"""Anagram exercise."""


def find_anagrams(word, candidates):
    """Check the list for anagrams and return them in a list."""
    target = word.lower()
    target_word = sorted(target)
    return [
        c
        for c in candidates
        if target != c.lower() and target_word == sorted(c.lower())
    ]
