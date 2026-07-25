"""Spiral matrix."""


def spiral_matrix(size: int) -> list[list[int]]:
    """Create a spiral matrix."""
    if size == 0:
        return []
    grid = [[0] * size for _ in range(size)]
    top_wall = 0
    right_wall = size - 1
    bottom_wall = size - 1
    left_wall = 0
    current_number = 1
    while current_number <= size * size:
        for col in range(left_wall, right_wall + 1):
            grid[top_wall][col] = current_number
            current_number += 1
        top_wall += 1
        for row in range(top_wall, bottom_wall + 1):
            grid[row][right_wall] = current_number
            current_number += 1
        right_wall -= 1
        for col in range(right_wall, left_wall - 1, -1):
            grid[bottom_wall][col] = current_number
            current_number += 1
        bottom_wall -= 1
        for row in range(bottom_wall, top_wall - 1, -1):
            grid[row][left_wall] = current_number
            current_number += 1
        left_wall += 1
    return grid
