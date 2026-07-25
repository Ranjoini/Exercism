"""Code for the rotational cypher exercise."""

import string


def rotate(text: str, key: int) -> str:
    """Create a cypher text."""
    lower_alpha = string.ascii_lowercase
    upper_alpha = string.ascii_uppercase
    cipher_text = ""
    for char in text:
        if char.islower():
            current_index = lower_alpha.index(char)
            new_index = (current_index + key) % 26
            cipher_text += lower_alpha[new_index]
        elif char.isupper():
            current_index = upper_alpha.index(char)
            new_index = (current_index + key) % 26
            cipher_text += upper_alpha[new_index]
        else:
            cipher_text += char
    return cipher_text
