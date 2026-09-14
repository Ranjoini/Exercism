def primes(limit: int) -> list[int]:
    prime_list = []
    marked = set()
    for number in range(2, limit + 1):
        if number not in marked:
            prime_list.append(number)
            for multiples in range(number * 2, limit + 1, number):
                marked.add(multiples)
    return prime_list
