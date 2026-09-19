"""Book store exercsie solved using dynamic programming."""

from collections import Counter


def total(basket: list[int]) -> int:
    # created a pricing map in cents
    PRICES = {0: 0, 1: 800, 2: 1520, 3: 2160, 4: 2560, 5: 3000}
    # Compress the basket into groups
    compressed_bskt = tuple(sorted(Counter(basket).values(), reverse=True))
    # Memory incase we have a similar compressed map, we can just take the pricing from here
    memo = {}

    def calculate_min(state: tuple[int, ...]) -> int:
        """Calculate the min price for each price group."""
        if not state:
            return 0
        # Checks for the compressed_bskt in Memory
        if state in memo:
            return memo[state]
        min_cost = float("inf")
        # How many different titles do we have
        titles = len(state)
        for group_size in range(1, titles + 1):
            new_state_list = list(state)
            for i in range(group_size):
                new_state_list[i] -= 1
            leftover_bskt = tuple(
                sorted([c for c in new_state_list if c > 0], reverse=True)
            )

            # Calculate the cost of the group size omitted plus the leftover_bskt cost
            cost = PRICES[group_size] + calculate_min(leftover_bskt)
            min_cost = min(min_cost, cost)
        memo[state] = int(min_cost)
        return int(min_cost)

    return calculate_min(compressed_bskt)
