def square_root(number):
    low = 1
    high = number
    while low <= high:
        mid_point = (low + high) // 2
        square = mid_point**2
        if square == number:
            return mid_point
        if square > number:
            high = mid_point - 1
        if square < number:
            low = mid_point + 1
