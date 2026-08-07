"""Change exercise."""


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Use dynamic programming to find the least combination of coins for target."""
    if target < 0:
        raise ValueError("target can't be negative")

    tracker: list[list[int] | None] = [None] * (target + 1)
    tracker[0] = []

    for coin in coins:
        for amount in range(coin, target + 1):
            leftover = amount - coin

            leftover_combo = tracker[leftover]
            if leftover_combo is not None:
                new_combo = leftover_combo + [coin]
                current_combo = tracker[amount]
                if current_combo is None or len(new_combo) < len(current_combo):
                    tracker[amount] = new_combo
    final_combo = tracker[target]

    if final_combo is None:
        raise ValueError("can't make target with given coins")
    return final_combo
