def steps(number):
    """Calculate the number of steps to reach 1 using the Collatz conjecture."""
    if number <= 0: raise ValueError("Only positive integers are allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1 
        count += 1
    return count 
