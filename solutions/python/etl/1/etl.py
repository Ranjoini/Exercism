"""ETL."""


def transform(legacy_data: dict) -> dict:
    """Transform the legacy data formatting to an indvivdualized kind of format."""
    return {
        letter.lower(): score
        for score, letters in legacy_data.items()
        for letter in letters
    }
