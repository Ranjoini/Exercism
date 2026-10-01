import math
from typing import Generator


def largest_product(series, size):
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    for digit in series:
        if not digit.isdigit():
            raise ValueError("digits input must only contain digits")
    integer_list = [int(digit) for digit in series]

    def product_generator() -> Generator[int, None, None]:
        for i in range(len(integer_list) - size + 1):
            chunk = integer_list[i : i + size]
            yield math.prod(chunk)

    return max(product_generator())
