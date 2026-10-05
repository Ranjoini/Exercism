"""Food Chain exercise."""


class Foodchain:
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

    def build_verse(self, verse_num):
        index = verse_num - 1
        animal, reaction = self.ANIMALS[index]

        yield f"I know an old lady who swallowed a {animal}."
        if reaction:
            yield reaction
        if animal == "horse":
            return
        for i in range(index, 0, -1):
            current_animal = self.ANIMALS[i][0]
            prev_animal = self.ANIMALS[i - 1][0]
            chain_line = (
                f"She swallowed the {current_animal} to catch the {prev_animal}"
            )
            if prev_animal == "spider":
                spider_reaction = self.ANIMALS[i - 1][1].replace("It", "that")
                chain_line += f" {spider_reaction}"
            else:
                chain_line += "."
            yield chain_line
        yield "I don't know why she swallowed the fly. Perhaps she'll die."

    def recite(self, start_verse, end_verse):
        for verse in range(start_verse, end_verse + 1):
            yield from self.build_verse(verse)
            if verse != end_verse:
                yield ""


def recite(start_verse, end_verse):
    engine = Foodchain()
    return list(engine.recite(start_verse, end_verse))
