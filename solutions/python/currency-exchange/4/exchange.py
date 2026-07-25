"""
Module for processing currency exchange calculations with integer and precise float math.
"""


def exchange_money(budget: float, exchange_rate: float) -> float:
    """Calculates value of exchanged currency."""
    return budget / exchange_rate


def get_change(budget: float, exchanging_value: float) -> float:
    """Calculates remaining budget after exchanging a specific value."""
    return budget - exchanging_value


def get_value_of_bills(denomination: int, number_of_bills: int) -> int:
    """Computes total value of a specific quantity of physical bills."""
    return denomination * number_of_bills


def get_number_of_bills(amount: float, denomination: int) -> int:
    """Calculates the maximum number of whole bills that can be received."""
    return int(amount // denomination)


def get_leftover_of_bills(budget: float, denomination: int) -> float:
    """Computes the leftover amount that cannot be exchanged into whole bills."""
    return budget % denomination


def exchangeable_value(
    budget: float, exchange_rate: float, spread: float, denomination: int
) -> int:
    """
    Calculates maximum exchangeable value inside whole bill denominations,
    incorporating exchange fees (spread).
    """
    # 1. Calculate actual rate with spread applied
    actual_rate = exchange_rate * (1 + (spread / 100))

    # 2. Get the raw total currency allocation
    total_currency = budget / actual_rate

    # 3. Use integer division to get exact bill count, then scale back up
    number_of_bills = int(total_currency // denomination)

    return number_of_bills * denomination
