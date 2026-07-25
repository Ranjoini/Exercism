"""Functions to keep track and alter inventory."""

from collections import Counter


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    return dict(Counter(items))


def add_items(inventory, items):
    """Add or increment items in inventory using elements from the items `list`."""
    for item in items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def decrement_items(inventory, items):
    """Decrement items in inventory using elements from the `items` list."""
    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory


def remove_item(inventory, item):
    """Remove item from inventory if it matches `item` string."""
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory):
    """Create list of available items using a comprehension expression."""
    return [(item, count) for item, count in inventory.items() if count > 0]
