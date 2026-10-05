class House:
    PARTS = (
        ("house that Jack built.", ""),
        ("malt", "that lay in"),
        ("rat", "that ate"),
        ("cat", "that killed"),
        ("dog", "that worried"),
        ("cow with the crumpled horn", "that tossed"),
        ("maiden all forlorn", "that milked"),
        ("man all tattered and torn", "that kissed"),
        ("priest all shaven and shorn", "that married"),
        ("rooster that crowed in the morn", "that woke"),
        ("farmer sowing his corn", "that kept"),
        ("horse and the hound and the horn", "that belonged to"),
    )

    def build_verse(self, verse_num):
        index = verse_num - 1
        verse_text = f"This is the {self.PARTS[index][0]}"
        for i in range(index, 0, -1):
            action = self.PARTS[i][1]
            prev_noun = self.PARTS[i - 1][0]
            verse_text += f" {action} the {prev_noun}"
        yield verse_text

    def recite(self, start_verse, end_verse):
        for verse in range(start_verse, end_verse + 1):
            yield from self.build_verse(verse)


def recite(start_verse, end_verse):
    engine = House()
    return list(engine.recite(start_verse, end_verse))
