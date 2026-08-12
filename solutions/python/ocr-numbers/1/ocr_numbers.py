OCR_DICT = {
    (" _ ", "| |", "|_|", "   "): "0",
    ("   ", "  |", "  |", "   "): "1",
    (" _ ", " _|", "|_ ", "   "): "2",
    (" _ ", " _|", " _|", "   "): "3",
    ("   ", "|_|", "  |", "   "): "4",
    (" _ ", "|_ ", " _|", "   "): "5",
    (" _ ", "|_ ", "|_|", "   "): "6",
    (" _ ", "  |", "  |", "   "): "7",
    (" _ ", "|_|", "|_|", "   "): "8",
    (" _ ", "|_|", " _|", "   "): "9",
}


def convert(input_grid):
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")
    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError("Number of input columns is not a multiple of three")
    results = []
    for i in range(0, len(input_grid), 4):
        row_group = input_grid[i : i + 4]
        current_row_digits = ""
        for j in range(0, len(row_group[0]), 3):
            cell = (
                row_group[0][j : j + 3],
                row_group[1][j : j + 3],
                row_group[2][j : j + 3],
                row_group[3][j : j + 3],
            )
            current_row_digits += OCR_DICT.get(cell, "?")
        results.append(current_row_digits)
    return ",".join(results)
