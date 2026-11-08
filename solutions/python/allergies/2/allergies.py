from typing import ClassVar


class Allergies:
    ALLERGENS: ClassVar[list[str]] = [
        "eggs",
        "peanuts",
        "shellfish",
        "strawberries",
        "tomatoes",
        "chocolate",
        "pollen",
        "cats",
    ]

    def __init__(self, score):
        self.allergens = [
            allergen
            for index, allergen in enumerate(Allergies.ALLERGENS)
            if (score & (1 << index))
        ]

    def allergic_to(self, item):
        """Check for the specific allergen in the list."""
        return item in self.allergens

    @property
    def lst(self):
        """Return a list of all allergens in the list."""
        return self.allergens
