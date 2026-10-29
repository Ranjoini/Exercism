"""Queen attack py."""


class Queen:
    def __init__(self, row, column):
        # ValueError hadnling before assigning row and column to instance dictionary
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")
        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        """Check if it is possible for the queens to capture each other."""
        # Chained the postion checking into a tuple, to avoid writing another if statement.
        if (self.row, self.column) == (another_queen.row, another_queen.column):
            raise ValueError("Invalid queen position: both queens in the same square")
        # Compiled the code into the return statement since "==" still evaluates to a boolean equation.
        return (
            self.row == another_queen.row
            or self.column == another_queen.column
            or abs(self.row - another_queen.row)
            == abs(self.column - another_queen.column)
        )
