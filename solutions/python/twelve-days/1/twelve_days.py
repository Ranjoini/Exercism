"""Twelve days exercise."""

ORDINALS = [
    None,
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

GIFTS = [
    None,
    "a Partridge in a Pear Tree.",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]


def build_verse(day):
    """Recives the day and inputs all the info in the lists we created in the format of the song."""
    intro = f"On the {ORDINALS[day]} day of Christmas my true love gave to me: "
    daily_gifts = GIFTS[day:0:-1]

    if day > 1:
        daily_gifts[-1] = "and " + daily_gifts[-1]

    return intro + ", ".join(daily_gifts)


def recite(start_verse, end_verse):
    """Just a range function used to give the verses required."""
    # The + 1 ensures the range includes the end_verse!
    return [build_verse(day) for day in range(start_verse, end_verse + 1)]
