import math


def largest_product(series, size):
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    for digit in series:
        if not digit.isdigit():
            raise ValueError("digits input must only contain digits")
    integer_list = [int(digit) for digit in series]
    products = []
    for i in range(len(integer_list) - size + 1):
        chunk = integer_list[i : i + size]
        chunk_product = math.prod(chunk)
        products.append(chunk_product)
    return max(products)
