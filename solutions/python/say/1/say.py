"""Say exercise."""

# Map out dictionaries, one for the ones and teens, the other for the Tens
ONES_TEENS = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}
TENS = {
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}


def translate(num: int) -> str:
    """Translate numbers under 1000."""
    if num < 20:
        return ONES_TEENS[num]
    elif num < 100:
        tens, remainder = divmod(num, 10)
        tens_word = TENS[tens * 10]
        if remainder == 0:
            return tens_word
        else:
            return f"{tens_word}-{ONES_TEENS[remainder]}"
    else:
        hundreds, remainder = divmod(num, 100)
        hundreds_word = f"{ONES_TEENS[hundreds]} hundred"
        if remainder == 0:
            return hundreds_word
        else:
            return f"{hundreds_word} {translate(remainder)}"


def say(number: int) -> str:
    """Split number to chunks of 3, feed to translate then return product."""
    # Edge cases
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    if number == 0:
        return "zero"
    magnitudes = ["", "thousand", "million", "billion"]
    word_chuncks = []
    magnitude_index = 0
    while number > 0:
        number, chunk = divmod(number, 1000)
        if chunk > 0:
            words = translate(chunk)
            if magnitudes[magnitude_index]:
                word_chuncks.append(f"{words} {magnitudes[magnitude_index]}")
            else:
                word_chuncks.append(words)
        magnitude_index += 1
    return " ".join(reversed(word_chuncks))
