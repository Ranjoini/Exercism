"""Saddle points exercise."""


def saddle_points(matrix):
    """Find the snallest tree in its column and the biggest tree in its row."""
    # Loop through the matrix to see if it is irregular
    if not matrix:
        return []
    expected_length = len(matrix[0])
    for row in matrix:
        if len(row) != expected_length:
            raise ValueError("irregular matrix")
    # The lists we will use to check for the max row and min col
    row_maxs = [max(row) for row in matrix]
    col_mins = [min(col) for col in zip(*matrix)]
    result = []
    # Loop through the rows(r = row index, row = the list of trees)
    for r, row in enumerate(matrix):
        # Loop through the columns in that row (c = column index, tree = the height)
        for c, _ in enumerate(row):
            if row_maxs[r] == col_mins[c]:
                result.append({"row": r + 1, "column": c + 1})
    return result
