"""Spiral matrix."""


def spiral_matrix(size: int) -> list[list[int]]:
    """Create a spiral matrix."""
    if size == 0:
        return []
    grid = [[0] * size for _ in range(size)]
    pos = 0 + 0j
    direction = 1 + 0j
    for current_num in range(1, size * size + 1):
        r, c = int(pos.imag), int(pos.real)
        grid[r][c] = current_num
        next_pos = pos + direction
        next_r, next_c = int(next_pos.imag), int(next_pos.real)
        if not (
            0 <= next_r < size and 0 <= next_c < size and grid[next_r][next_c] == 0
        ):
            direction *= 1j
        pos += direction
    return grid
