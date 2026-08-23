"""Dominoes exercise."""


def can_chain(dominoes):
    """Check for the vacuous truth."""
    if not dominoes:
        return []

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
            left, right = domino
            if left == target:
                updated_pool = pool[:pos] + pool[pos + 1 :]
                updated_chain = chain + [(left, right)]
                result = build_chain(updated_chain, updated_pool)
                if result:
                    return result

            if right == target:
                updated_pool = pool[:pos] + pool[pos + 1 :]
                updated_chain = chain + [(right, left)]
                result = build_chain(updated_chain, updated_pool)
                if result:
                    return result
        return None

    # IGNITION STEP !
    chain_starter = [dominoes[0]]
    starting_pool = dominoes[1:]
    return build_chain(chain_starter, starting_pool)
