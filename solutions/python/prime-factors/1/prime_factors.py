def factors(value: int) -> list[int]:
    prime_factors = []
    divisor = 2
    while value > 1:
        quotient, remainder = divmod(value, divisor)
        if remainder == 0:
            prime_factors.append(divisor)
            value = quotient
        else:
            divisor += 1
    return prime_factors
