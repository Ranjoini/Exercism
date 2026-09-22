import itertools


def transpose(text: str) -> str:
    if not text:
        return ""
    lines = text.splitlines()
    padded_lines = []
    for i, line in enumerate(lines):
        max_width = max(len(l) for l in lines[i:])
        padded_lines.append(
            line.ljust(
                max_width,
            )
        )
    columns = itertools.zip_longest(*padded_lines, fillvalue="")
    return "\n".join("".join(char) for char in columns)
