"""
Module for high-performance inventory management.
Leverages native Counter arithmetic operators to eliminate manual loop processing.
"""

from collections import Counter
from typing import Dict, List, Tuple


def create_inventory(items: List[str]) -> Dict[str, int]:
    """Generates a standard dictionary tracking the frequency of items."""
    return dict(Counter(items))


def add_items(inventory: Dict[str, int], items: List[str]) -> Dict[str, int]:
    """
    Increments inventory quantities using native Counter addition.
    Eliminates manual loop overhead.
    """
    # Convert both sides to Counters, add them natively, cast back to dict
    combined = Counter(inventory) + Counter(items)

    # Mutate the original dictionary in-place to preserve reference identity
    inventory.clear()
    inventory.update(combined)
    return inventory


def decrement_items(inventory: dict[str, int], items: list[str]) -> dict[str, int]:
    """
    Decrement items in inventory using elements from the `items` list.
    Locks values at 0 instead of letting them drop below or disappear.
    """
    for item in items:
        if item in inventory:
            # Drop the value by 1, but use max() to ensure it never falls below 0
            inventory[item] = max(0, inventory[item] - 1)
    return inventory


def remove_item(inventory: Dict[str, int], item: str) -> Dict[str, int]:
    """Permanently purges a specific item entry from the inventory catalog."""
    inventory.pop(item, None)
    return inventory


def list_inventory(inventory: Dict[str, int]) -> List[Tuple[str, int]]:
    """Generates a filtered listing of all active stock configurations."""
    return [(item, count) for item, count in inventory.items() if count > 0]
