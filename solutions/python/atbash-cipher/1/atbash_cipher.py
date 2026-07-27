"""ATBASH_CIPHER."""

import string

alphabet = string.ascii_lowercase
reversed_alphabet = alphabet[::-1]
ATBASH_CIPHER = str.maketrans(alphabet, reversed_alphabet)


def encode(plain_text: str) -> str:
    """Translate regular text to atbash cipher."""
    clean_text = "".join(char.lower() for char in plain_text if char.isalnum())
    translated_text = clean_text.translate(ATBASH_CIPHER)
    chunks = [translated_text[i : i + 5] for i in range(0, len(translated_text), 5)]
    return " ".join(chunks)


def decode(ciphered_text: str) -> str:
    """Translate atbash cipher text to regular text."""
    clean_text = "".join(char for char in ciphered_text if char.isalnum())
    translated_text = clean_text.translate(ATBASH_CIPHER)
    return translated_text
