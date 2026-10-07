def line_up(name, number):
    prefix = "th"
    str_num = str(number)
    if str_num.endswith("1"):
        prefix = "st"
    if str_num.endswith("2"):
        prefix = "nd"
    if str_num.endswith("3"):
        prefix = "rd"
    if str_num.endswith("11"):
        prefix = "th"
    if str_num.endswith("12"):
        prefix = "th"
    if str_num.endswith("13"):
        prefix = "th"

    return f"{name}, you are the {number}{prefix} customer we serve today. Thank you!"
