def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")

    def prime_generator():
        yield 2
        candidate = 3
        while True:
            is_prime = True
            limit = int(candidate**0.5) + 1
            for i in range(3, limit, 2):
                if candidate % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield candidate
            candidate += 2

    engine = prime_generator()
    nth_prime = 0
    for _ in range(number):
        nth_prime = next(engine)
    return nth_prime
