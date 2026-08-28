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
    """Translate the number to roman numerals."""
    result = ""
    for value, numerals in ROMAN_MAPPING:
        while number >= value:
            result += numerals
            number -= value
    return result
