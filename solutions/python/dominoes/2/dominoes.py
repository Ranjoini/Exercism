"""Dominoes exercise."""


def can_chain(dominoes):
    """Check for the vacuous truth."""
    if not dominoes:
        return []
    # OPTIMIZATION
    # Flatten all dominoes into one giant list of numbers
    all_numbers = [num for domino in dominoes for num in domino]
    # If any number appears an odd number of times a closed loop in impossible.
    for num in set(all_numbers):
        if all_numbers.count(num) % 2 != 0:
            return None

    def build_chain(chain, pool):
        """Use a backtracking method to go back from where you got lost and find another route."""
        # STEP 3
        # if pool is empty it means that all dominoes have been placed on the track.
        if not pool:
            # compare the face of the rightmost domino's right side with the leftmost domino left side to see if they match.
            if chain[0][0] == chain[-1][1]:
                return chain
            else:
                return None
        # STEP 2
        # set our target domino that will be used to match the sides of the other dominoes
        target = chain[-1][1]
        for pos, domino in enumerate(pool):
            if target in domino:
                new_pool = pool[:pos] + pool[pos + 1 :]
                if domino[0] == target:
                    new_chain = chain + [domino]
                else:
                    new_chain = chain + [domino[::-1]]
                result = build_chain(new_chain, new_pool)
                if result:
                    return result
        return None

    # IGNITION STEP !
    return build_chain([dominoes[0]], dominoes[1:])
