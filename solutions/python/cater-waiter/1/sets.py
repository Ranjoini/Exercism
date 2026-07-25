"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)


def clean_ingredients(
    dish_name: str, dish_ingredients: list[str]
) -> tuple[str, set[str]]:
    """Clean a dish's ingredient assembly line by removing all duplicates."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name: str, drink_ingredients: list[str]) -> str:
    # Ensure 'return' is placed before the f-string output choice
    overlapping_ingredients = set(drink_ingredients) & ALCOHOLS
    if overlapping_ingredients:
        return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name: str, dish_ingredients: list[str]) -> str:
    """Classify a dish into its correct dietary category using subset mapping."""
    # 1. Cast the incoming assembly line to a clean set for optimized hashing lookups
    ingredients_set = set(dish_ingredients)

    # 2. Decoupled Matrix: Order matters! We map labels to their respective specification targets.
    # (Vegan is checked before Vegetarian because all Vegan dishes are technically Vegetarian, but not vice versa)
    diet_matrix = [
        ("VEGAN", VEGAN),
        ("VEGETARIAN", VEGETARIAN),
        ("PALEO", PALEO),
        ("KETO", KETO),
        ("OMNIVORE", OMNIVORE),
    ]

    # 3. Dynamic Lookup Loop
    for category_name, diet_spec in diet_matrix:
        # Check if every ingredient in the dish is a subset of the target dietary spec
        if ingredients_set <= diet_spec:
            return f"{dish_name}: {category_name}"

    # Precision Error Catch: If it completely bypasses the matrix without matching anything
    raise ValueError(
        f"Classification Fault: Dish '{dish_name}' does not align with any known dietary profile."
    )


def tag_special_ingredients(
    dish: tuple[str, list[str] | set[str]],
) -> tuple[str, set[str]]:
    """Isolate allergens present in a dish using a clean tuple one-liner."""
    return (dish[0], set(dish[1]) & SPECIAL_INGREDIENTS)


def compile_ingredients(
    dishes: list[tuple[str, list[str] | set[str]] | list[str] | set[str]],
) -> set[str]:
    """Aggregate all ingredients into a single master set dynamically.

    Defends against fluctuating input data layouts via inline type evaluation.
    """
    master_ingredients = set()

    for item in dishes:
        # If the item is a tuple/list pair containing a dish name (like Task 1 output)
        if isinstance(item, tuple):
            master_ingredients.update(item[1])
        # If the item is a raw set or list of ingredients directly
        else:
            master_ingredients.update(item)

    return master_ingredients


def separate_appetizers(dishes: list[str], appetizers: list[str]) -> list[str]:
    """Filter out appetizers and return a unique list using a single expression."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes: list[set[str]], intersections: set[str]) -> set[str]:
    """Isolate singleton ingredients using an unpacked set union one-liner."""
    return set.union(*dishes) - intersections if dishes else set()
