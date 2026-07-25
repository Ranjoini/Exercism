"""
Module for coordinate conversion and record matching for treasure tracking.
Fully compliant with strict PEP 8 naming conventions and Pyright type analysis.
"""

from typing import Tuple, List, Union


def get_coordinate(record: Tuple[str, str]) -> str:
    """Extract the coordinate from a treasure hunt record."""
    _, coordinate = record
    return coordinate


def convert_coordinate(coordinate: str) -> Tuple[str, str]:
    """
    Convert a coordinate string into a tuple of component characters.
    Explicit indexing guarantees a fixed-length 2-tuple for Pyright.
    """
    # This prevents Pyright from treating the output as an arbitrary-length tuple
    return (coordinate[0], coordinate[1])


def compare_records(
    azara_record: Tuple[str, str], rui_record: Tuple[str, Tuple[str, str], str]
) -> bool:
    """Compare two record types and determine if their coordinates match."""
    _, azara_coord = azara_record
    _, rui_coord, _ = rui_record
    return convert_coordinate(azara_coord) == rui_coord


def create_record(
    azara_record: Tuple[str, str], rui_record: Tuple[str, Tuple[str, str], str]
) -> Union[Tuple[str, str, str, Tuple[str, str], str], str]:
    """Combine treasure and location records if their coordinates match."""
    if compare_records(azara_record, rui_record):
        return azara_record + rui_record
    return "not a match"


def clean_up(
    combined_record_group: List[Tuple[str, str, str, Tuple[str, str], str]],
) -> str:
    """
    Streamlined clean up using a comprehension expression.
    Variable 'location' replaces ambiguous single-character 'l' to satisfy Ruff.
    """
    # Renamed 'l' to 'location' to eliminate ambiguity
    cleaned = [
        str((treasure, location, coordinate_tuple, color))
        for treasure, _, location, coordinate_tuple, color in combined_record_group
    ]
    return "\n".join(cleaned) + "\n"
