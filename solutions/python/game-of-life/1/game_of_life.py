OFFSETS = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (
        1,
        -1,
    ),
    (1, 0),
    (1, 1),
]


def count_live_neighbours(matrix, row, col):
    """Create a helper function to count the live and deaf cells."""
    live_count = 0
    # Used to define maximum boundary for coordinates row and col
    rows = len(matrix)
    # intorduced the if/else to check if rows > 0, avoids IndexErrors
    cols = len(matrix[0]) if rows > 0 else 0
    for r_offset, c_offset in OFFSETS:
        new_row = row + r_offset
        new_col = col + c_offset
        # Boundary restriction if either the row or col is less than 0 or greater than rows or col
        if 0 <= new_row < rows and 0 <= new_col < cols:
            live_count += matrix[new_row][new_col]
    return live_count


def tick(matrix):
    """Create the new matrix."""
    if not matrix:
        return []
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []
    for r in range(rows):
        new_row = []
        for c in range(cols):
            live_neighbours = count_live_neighbours(matrix, r, c)
            current_cell = matrix[r][c]
            if (
                current_cell == 1
                and live_neighbours in (2, 3)
                or current_cell == 0
                and live_neighbours == 3
            ):
                new_row.append(1)
            else:
                new_row.append(0)
        new_matrix.append(new_row)
    return new_matrix
