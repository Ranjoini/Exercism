"""Perfect numbers exercise."""


def classify(number: int) -> str:
    """Determine if a number is perfect, abundant, or deficient based on Nicomachus' (60 - 120 CE) classification scheme for positive integers."""
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    factors = [i for i in range(1, number) if number % i == 0]
    aliquot_sum = sum(factors)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
