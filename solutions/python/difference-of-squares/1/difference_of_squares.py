def square_of_sum(number):
    val_a = (sum(num for num in range(1, number + 1))) ** 2
    return val_a


def sum_of_squares(number):
    val_b = sum(num**2 for num in range(1, number + 1))
    return val_b


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
