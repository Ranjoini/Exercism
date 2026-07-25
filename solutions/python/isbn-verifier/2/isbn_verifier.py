"""ISBN Verification."""


def is_valid(isbn: str) -> bool:
    """Check if it is a valid ISBN number."""
    clean_isbn = isbn.replace("-", "")
    if len(clean_isbn) != 10:
        return False
    total_sum = 0
    for index, char in enumerate(clean_isbn):
        multiplier = 10 - index
        if char == "X" and index == 9:
            total_sum += 10 * multiplier
        elif char.isdigit():
            total_sum += int(char) * multiplier
        else:
            return False
    return total_sum % 11 == 0
