"""ISBN Verification."""


def is_valid(isbn: str) -> bool:
    """Check if it is a valid ISBN number."""
    clean_isbn = isbn.replace("-", "")
    total_sum = 0
    multiplier = 10

    if len(clean_isbn) != 10:
        return False
    for char in clean_isbn:
        if char == "X" and multiplier == 1:
            total_sum += 10 * multiplier
        elif char.isdigit():
            total_sum += int(char) * multiplier
        else:
            return False
        multiplier -= 1
    return total_sum % 11 == 0
