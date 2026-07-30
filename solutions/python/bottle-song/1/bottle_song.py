"""Bottle song exercise."""

NUMBERS = [
    "no",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
]


def recite(start, take=1):
    song = []
    for bottles in range(start, start - take, -1):
        current_num_word = NUMBERS[bottles].capitalize()
        next_num_word = NUMBERS[bottles - 1]
        current_plural = "bottles"
        next_plural = "bottles"
        if bottles == 1:
            current_plural = "bottle"
        if bottles - 1 == 1:
            next_plural = "bottle"
        verse = [
            f"{current_num_word} green {current_plural} hanging on the wall,",
            f"{current_num_word} green {current_plural} hanging on the wall,",
            "And if one green bottle should accidentally fall,",
            f"There'll be {next_num_word} green {next_plural} hanging on the wall.",
        ]
        song.extend(verse)
        if bottles > start - take + 1:
            song.append("")
    return song
