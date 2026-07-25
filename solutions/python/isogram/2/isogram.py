"""Code for the exercise isogram py."""


def is_isogram(phrase):
    """Determine whether a word is an isogram."""
    lwrcase_text = phrase.lower()
    reference_manual = []
    for char in lwrcase_text:
        if char.isalpha():
            if char in reference_manual:
                return False
        reference_manual.append(char)
    return True
