"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagons."""
    return [*args]


def fix_list_of_wagons(
    each_wagons_id: list[int], missing_wagons: list[int]
) -> list[int]:
    """Reposition rogue wagons and insert missing IDs right behind locomotive 1."""
    # 1. Funnel-pack the glitched list layout into separate variables
    rogue_1, rogue_2, locomotive, *remaining_wagons = each_wagons_id

    # 2. Explode them back into the requested production sequence
    return [locomotive, *missing_wagons, *remaining_wagons, rogue_1, rogue_2]


def add_missing_stops(
    routing_dict: dict[str, str | list[str]], **kwargs: str
) -> dict[str, str | list[str]]:
    """Capture dynamic keyword stops and inject them into the routing profile."""
    # 1. Extract the values (cities) from the packed kwargs dict and convert them to a list
    added_stops = list(kwargs.values())

    # 2. Assign the new list to the "stops" key inside our primary dictionary
    routing_dict["stops"] = added_stops

    # 3. Return the updated master profile map
    return routing_dict


def extend_route_information(
    route: dict[str, str], more_route_information: dict[str, str]
) -> dict[str, str]:
    """Merge two route logistics dictionaries together using double-asterisk unpacking."""
    return {**route, **more_route_information}


def fix_wagon_depot(
    wagons_rows: list[list[tuple[int, str]]],
) -> list[list[tuple[int, str]]]:
    """Transpose the wagon depot grid layout so that columns align cleanly by color.

    Uses asterisk unpacking combined with the native zip engine.
    """
    # zip(*matrix) effortlessly switches rows to columns at the C-compiler level
    return [list(row) for row in zip(*wagons_rows)]
