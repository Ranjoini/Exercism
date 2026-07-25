"""All your base exercise."""


def rebase(input_base, digits, output_base):
    """Convert the digits to base 10."""
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    base10_value = 0
    for power, digit in enumerate(reversed(digits)):
        base10_value += digit * (input_base**power)
    if base10_value == 0:
        return [0]
    output_digits = []
    while base10_value > 0:
        remainder = base10_value % output_base
        output_digits.append(remainder)
        base10_value = base10_value // output_base
    return output_digits[::-1]
