"""Series exercise."""


def slices(series: str, length: int) -> list[str]:
    """Slice the series according to the length given and return the chunks as list[str]."""
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    sub_string = []
    index = 0
    while index <= len(series) - length:
        chunk = series[index : index + length]
        sub_string.append(chunk)
        index += 1  # Do not forget to shift to the next index caused an infinite loop on my end.
    return sub_string
