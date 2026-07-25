"""Functions to manage a user's shopping cart items."""


def add_item(current_cart: dict[str, int], items_to_add: list[str]) -> dict[str, int]:
    """
    Add samples from the items_to_add list into the current_cart dictionary.
    Modifies the existing dictionary in place instead of resetting it.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1
    return current_cart


def read_notes(notes: list[str]) -> dict[str, int]:
    """Create user cart from an iterable notes entry."""
    return {item: 1 for item in notes}


def update_recipes(
    ideas: dict[str, dict[str, int]], recipe_updates: list[tuple]
) -> dict[str, dict[str, int]]:
    """Update the recipe ideas dictionary using the merge operator."""
    return ideas | dict(recipe_updates)


def sort_entries(cart: dict[str, int]) -> dict[str, int]:
    """Sort items in shopper's cart alphabetically."""
    return {item: cart[item] for item in sorted(cart)}


def send_to_store(
    cart: dict[str, int], aisle_mapping: dict[str, list]
) -> dict[str, list]:
    """Combine quantity, aisle, and refrigeration data sorted from Z-to-A."""
    return {
        item: [cart[item]] + aisle_mapping[item] for item in sorted(cart, reverse=True)
    }


def update_store_inventory(
    fulfillment_cart: dict[str, list], store_inventory: dict[str, list]
) -> dict[str, list]:
    """
    Subtract ordered quantities from store inventory.
    Preserves the nested list layout even when stock drops to zero.
    """
    for item in fulfillment_cart:
        if item in store_inventory:
            ordered_amount = fulfillment_cart[item][0]
            store_inventory[item][0] -= ordered_amount

            # If stock hits 0, update the entry at index 0 to 'Out of Stock'
            # This preserves the rest of the list ([1] aisle, [2] refrigeration)
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = "Out of Stock"

    return store_inventory
