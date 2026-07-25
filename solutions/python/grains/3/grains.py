"""Calculate the number of grains on each square and their total number."""
def square(number):
    """Calculate the number of grains on each square."""
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
def total():
    """Calculate the total number of grains."""
    return (2 ** 64) - 1 
