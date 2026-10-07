SUFFIX = {1: "st", 2: "nd", 3: "rd"}


def line_up(name, number):
    _, remainder = divmod(number, 100)
    if remainder in [11, 12, 13]:
        suffix = "th"
    else:
        target = remainder % 10
        suffix = SUFFIX.get(target, "th")

    return f"{name}, you are the {number}{suffix} customer we serve today. Thank you!"
