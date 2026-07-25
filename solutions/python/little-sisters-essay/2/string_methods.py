"""
Module for editing essay text structures via advanced string manipulation.
Optimized for native execution and explicit type checking.
"""


def capitalize_title(title: str) -> str:
    """
    Capitalizes the first letter of each word in a title.
    Uses a clean generator to avoid the native .title() apostrophe capitalization bug
    without importing the external 'string' module.
    """
    return " ".join(word.capitalize() for word in title.split(" "))


def check_sentence_ending(sentence: str) -> bool:
    """Verifies if the sentence terminates with a valid period marker."""
    return sentence.endswith(".")


def clean_up_spacing(sentence: str) -> str:
    """Removes all leading and trailing whitespace characters from the text string."""
    return sentence.strip()


def replace_word_choice(sentence: str, old_word: str, new_word: str) -> str:
    """Replaces all occurrences of a target substring with a designated replacement string."""
    return sentence.replace(old_word, new_word)
