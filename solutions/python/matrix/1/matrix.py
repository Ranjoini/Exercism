class Matrix:
    def __init__(self, matrix_string):
        self.grid = []
        for line in matrix_string.splitlines():
            row_data = [int(number) for number in line.split()]
            self.grid.append(row_data)

    def row(self, index):
        return self.grid[index - 1]

    def column(self, index):
        return [row_data[index - 1] for row_data in self.grid]
