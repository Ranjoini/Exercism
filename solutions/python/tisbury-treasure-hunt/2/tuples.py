"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record: tuple[str, str]) -> str:
    """Extract the coordinate from a treasure hunt record."""
    _, coordinate = record
    return coordinate


def convert_coordinate(coordinate: str) -> tuple[str, str]:
    """Convert a coordinate string into a tuple of component characters."""
    return tuple(coordinate)

def compare_records(azara_record: tuple[str , str], rui_record: tuple[str , tuple[ str , str] , str]) -> bool:
    """Compare two record types and determine if their coordinates match."""
    _, azara_coord = azara_record
    _, rui_coord , _ = rui_record
    return convert_coordinate(azara_coord) == rui_coord


def create_record(azara_record: tuple[str, str] , rui_record: tuple[str, tuple[str, str], str]) -> tuple[str, str, str, tuple[str, str], str] | str:
    """Combine treasure and location records if their coordinates match."""
    if compare_records(azara_record , rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(combined_record_group: tuple) -> str:
    """Streamlined clean up using a comprehension expression."""
    cleaned = [str((t, l, ct, c)) for t, _, l, ct, c in combined_record_group]
    return "\n" .join(cleaned) +  "\n"
