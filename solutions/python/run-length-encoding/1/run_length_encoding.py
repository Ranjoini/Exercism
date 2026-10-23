"""Run length encoding exercise."""


def decode(string: str) -> str:
    """Decode the text."""
    if not string:
        return ""
    index = 0
    result = []
    # to handle numbers which are more than one digit
    digit_accumulator = ""
    while index < len(string):
        if string[index].isdigit():
            digit_accumulator += string[index]
            index += 1
        else:
            if digit_accumulator:
                result.append(string[index] * int(digit_accumulator))
            else:
                result.append(string[index])
            digit_accumulator = ""
            index += 1
    return "".join(result)


def encode(string: str) -> str:
    """Enocode the text."""
    if not string:
        return ""
    result = []
    current_char = string[0]
    count = 1
    # Used None as a place-holder for the last item
    for char in list(string[1:]) + [None]:
        if char == current_char:
            count += 1
        else:
            if count > 1:
                result.append(f"{count}{current_char}")
            else:
                result.append(current_char)
            current_char = char
            count = 1
    return "".join(result)
