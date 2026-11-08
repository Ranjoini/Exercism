from typing import ClassVar


class Allergies:
    ALLERGEN_DICT: ClassVar[dict[str, int]] = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        """Check for the specific allergen in the score."""
        # Evaluates a bitwise check
        return bool(self.score & self.ALLERGEN_DICT[item])

    @property
    def lst(self):
        """Return a list of all allergens in the score."""
        return [
            allergen
            for allergen, value in self.ALLERGEN_DICT.items()
            if self.score & value
        ]
