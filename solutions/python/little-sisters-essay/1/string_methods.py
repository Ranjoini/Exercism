"""Functions to help edit essay homework using string manipulation."""

import string 

def capitalize_title(title):
    """Capitalize first letter of each word in title"""
    return string.capwords(title)


def check_sentence_ending(sentence):
    """Check if the sentence ends with a period."""
    return sentence.endswith(".")


def clean_up_spacing(sentence):
    """Remove white space at the end of the sentense"""
    return sentence.strip()


def replace_word_choice(sentence, old_word, new_word):
    """Replace adjectives with their synonyms"""
    return sentence.replace(old_word , new_word)
