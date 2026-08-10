"""Change exercise."""


def find_fewest_coins(coins: list[int], target: int) -> list[int]:
    """Use dynamic programming to find the least combination of coins for target."""
    if target < 0:
        raise ValueError("target can't be negative")
    if target == 0:
        return []
    min_coins = [float("inf")] * (target + 1)
    last_coin = [0] * (target + 1)
    min_coins[0] = 0

    for coin in coins:
        for amount in range(coin, target + 1):
            leftover = amount - coin
            if min_coins[leftover] != float("inf"):
                if min_coins[leftover] + 1 < min_coins[amount]:
                    min_coins[amount] = min_coins[leftover] + 1
                    last_coin[amount] = coin
    if min_coins[target] == float("inf"):
        raise ValueError("can't make target with given coins")
    result = []
    current_amount = target
    while current_amount > 0:
        coin_used = last_coin[current_amount]
        result.append(coin_used)
        current_amount -= coin_used
    return sorted(result)
