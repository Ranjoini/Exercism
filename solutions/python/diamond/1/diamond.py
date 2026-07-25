"""Diamond exercise."""

import string


def rows(letter: str) -> list[str]:
    """Create a diamond using letters."""
    alphabet = string.ascii_uppercase
    max_idx = alphabet.index(letter)
    top_half = []
    for i in range(max_idx + 1):
        # 1. Handling the 'A' row separately so that we do not end up with " A  A "
        if i == 0:
            top_half.append(" " * max_idx + alphabet[0] + " " * max_idx)
            continue
        # 2. Building the top half for the rest of the letters
        current_letter = alphabet[i]
        row_string = (
            " " * (max_idx - i)
            + current_letter
            + " " * (2 * i - 1)
            + current_letter
            + " " * (max_idx - i)
        )
        top_half.append(row_string)
    # 3. Mirroring the top_half to create the diamond structure
    return top_half + top_half[:-1][::-1]
