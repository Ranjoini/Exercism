"""Word count."""

from collections import Counter


def count_words(sentence):
    """Standadize the text and build the counter."""
    sentence = sentence.lower()
    bad_punctuation = '!"#$%&()*+,-./:;<=>?@[]\\^_`{|}~'
    for char in bad_punctuation:
        sentence = sentence.replace(char, " ")
    raw_words = sentence.split()
    cleaned_words = []
    for word in raw_words:
        clean = word.strip("'")
        if clean != "":
            cleaned_words.append(clean)
    return dict(Counter(cleaned_words))
