"""Tournament exercise."""

from collections import defaultdict


def tally(rows):
    """Convert the info given in row into the table format required."""
    teams = defaultdict(lambda: {"W": 0, "D": 0, "L": 0})
    for row in rows:
        team_a, team_b, outcome = row.split(";")
        if outcome == "win":
            teams[team_a]["W"] += 1
            teams[team_b]["L"] += 1
        elif outcome == "loss":
            teams[team_b]["W"] += 1
            teams[team_a]["L"] += 1
        elif outcome == "draw":
            teams[team_a]["D"] += 1
            teams[team_b]["D"] += 1
    sortable_teams = []
    for name, stats in teams.items():
        stats["MP"] = stats["W"] + stats["D"] + stats["L"]
        stats["P"] = stats["W"] * 3 + stats["D"]
        sortable_teams.append((-stats["P"], name))
    sorted_teams = sorted(sortable_teams)
    table = ["Team                           | MP |  W |  D |  L |  P"]
    for _, name in sorted_teams:
        stats = teams[name]
        row = f"{name:<30} | {stats['MP']:>2} | {stats['W']:>2} | {stats['D']:>2} | {stats['L']:>2} | {stats['P']:>2}"
        table.append(row)
    return table
