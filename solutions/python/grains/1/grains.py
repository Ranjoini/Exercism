def square(number):
    """function for calculating the number of grains on each square"""
    if number <= 0 or number >= 65:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
def total():
    """Calculating the total number of grains"""
    return (2 ** 64) - 1 
