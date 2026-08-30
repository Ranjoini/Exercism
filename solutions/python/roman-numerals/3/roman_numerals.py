"""Roman numerals."""

ROMAN_MAPPING = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def roman(number: int) -> str:
    """Solved using recursive programming."""
    # 1. THE BASE CASE
    # If the number has been whittled down to 0, there is nothing left to convert.
    if number == 0:
        return ""

    # 2. THE RECURSIVE STEP
    for value, numeral in ROMAN_MAPPING:
        # We find the very first (largest) value that fits into our number
        if number >= value:
            # We glue that numeral to the front, and recursively call the function
            # to handle whatever is left over!
            return numeral + roman(number - value)
    raise ValueError("Cannot convert this number.")
