"""State of tic tac toe."""


def gamestate(board):
    """Check the state of the board."""
    # Count X and O across the entire board
    x_count = sum(row.count("X") for row in board)
    o_count = sum(row.count("O") for row in board)

    # The Checks
    if o_count > x_count:
        raise ValueError("Wrong turn order: O started")
    if x_count > o_count + 1:
        raise ValueError("Wrong turn order: X went twice")
    # Winner Checks
    columns = ["".join(col) for col in zip(*board)]
    diag1 = board[0][0] + board[1][1] + board[2][2]
    diag2 = board[0][2] + board[1][1] + board[2][0]

    def player_wins(player):
        """Check the win state or draw or game rules breach."""
        # Creates either 'XXX' or 'OOO'
        win_strk = player * 3
        if win_strk in board:
            return True
        if win_strk in columns:
            return True
        if win_strk in diag1 or win_strk in diag2:
            return True
        return False

    x_won = player_wins("X")
    o_won = player_wins("O")
    # --- PHASE 3: The Impossible Board Checks ---
    if x_won and o_won:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if x_won and x_count != o_count + 1:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    if o_won and x_count != o_count:
        raise ValueError(
            "Impossible board: game should have ended after the game was won"
        )

    # --- PHASE 4: The Final State ---
    if x_won:
        return "win"
    if o_won:
        return "win"
    if x_count + o_count == 9:
        return "draw"

    return "ongoing"
