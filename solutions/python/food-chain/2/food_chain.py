"""Food Chain exercise."""

ANIMALS = (
    ("fly", ""),
    ("spider", "It wriggled and jiggled and tickled inside her."),
    ("bird", "How absurd to swallow a bird!"),
    ("cat", "Imagine that, to swallow a cat!"),
    ("dog", "What a hog, to swallow a dog!"),
    ("goat", "Just opened her throat and swallowed a goat!"),
    ("cow", "I don't know how she swallowed a cow!"),
    ("horse", "She's dead, of course!"),
)


def build_verse(verse_num):
    """Build the specific verse."""
    index = verse_num - 1
    animal, reaction = ANIMALS[index]

    lines = [f"I know an old lady who swallowed a {animal}."]

    if reaction:
        lines.append(reaction)

    if animal == "horse":
        return lines

    for i in range(index, 0, -1):
        current_animal = ANIMALS[i][0]
        prev_animal = ANIMALS[i - 1][0]

        chain_line = f"She swallowed the {current_animal} to catch the {prev_animal}"

        if prev_animal == "spider":
            spider_reaction = ANIMALS[i - 1][1]
            chain_line += " " + spider_reaction.replace("It", "that")
        else:
            chain_line += "."

        lines.append(chain_line)

    lines.append("I don't know why she swallowed the fly. Perhaps she'll die.")
    return lines


def recite(start_verse, end_verse):
    """Range through the start and end verse and call our build_verse function."""
    final_lyrics = []

    for verse in range(start_verse, end_verse + 1):
        final_lyrics.extend(build_verse(verse))
        if verse != end_verse:
            final_lyrics.append("")
    return final_lyrics
