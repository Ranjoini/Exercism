"""Flower field."""


def board(garden):
    """Ckeck if the garden provided is a valid rectangle and if the characters within are spaces and stars."""
    if not garden:
        return []
    expected_width = len(garden[0])
    for row in garden:
        if len(row) != expected_width:
            raise ValueError("The board is invalid with current input.")
        for char in row:
            if char != " " and char != "*":
                raise ValueError("The board is invalid with current input.")


def annotate(garden):
    """Check for stars in the spaces horizontally, vertically or diagonally adjacent to the space."""
    grid = [list(row) for row in garden]
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_rows = len(grid)
    total_cols = len(grid[0])
    for r in range(total_rows):
        for c in range(total_cols):
            if grid[r][c] == " ":
                counter = 0
                for dr, dc in offsets:
                    target_r = r + dr
                    target_c = c + dc
                    if (0 <= target_r < total_rows) and (0 <= target_c < total_cols):
                        if grid[target_r][target_c] == "*":
                            counter += 1
                if counter > 0:
                    grid[r][c] = str(counter)
    return ["".join(row) for row in grid]
