def triplets_with_sum(number: int) -> list[list[int]]:
    """Use algebra to find the values of a, b and c."""
    triplets = []
    # 'a' can never be larger than a third of the total sum
    for a in range(1, ((number // 3) + 1)):
        numerator = (number**2) - (2 * number * a)
        denominator = (2 * number) - (2 * a)
        if numerator % denominator == 0:
            b = numerator // denominator
            c = number - a - b
            if a < b < c:
                triplets.append([a, b, c])
    return triplets
