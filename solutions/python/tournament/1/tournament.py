"""Tournament exercise."""


def tally(rows):
    """Convert the info given in row into the table format required."""
    teams = {}
    for row in rows:
        team_a, team_b, outcome = row.split(";")
        if team_a not in teams:
            teams[team_a] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        if team_b not in teams:
            teams[team_b] = {"MP": 0, "W": 0, "D": 0, "L": 0, "P": 0}
        teams[team_a]["MP"] += 1
        teams[team_b]["MP"] += 1
        if outcome == "win":
            teams[team_a]["W"] += 1
            teams[team_a]["P"] += 3
            teams[team_b]["L"] += 1
        elif outcome == "loss":
            teams[team_b]["W"] += 1
            teams[team_b]["P"] += 3
            teams[team_a]["L"] += 1
        elif outcome == "draw":
            teams[team_a]["D"] += 1
            teams[team_a]["P"] += 1
            teams[team_b]["D"] += 1
            teams[team_b]["P"] += 1
    sortable_teams = []
    for name, stats in teams.items():
        sortable_teams.append((-stats["P"], name))
    sorted_teams = sorted(sortable_teams)
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for _, name in sorted_teams:
        stats = teams[name]
        row = f"{name:<30} | {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}"
        table.append(row)
    return table
