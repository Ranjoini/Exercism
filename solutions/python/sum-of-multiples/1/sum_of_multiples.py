def sum_of_multiples(limit: int, multiples: list[int]) -> int:
    return sum(
        {
            multiple
            for base in multiples
            if base != 0
            for multiple in range(base, limit, base)
        }
    )
