import itertools


def proverb(*args, qualifier=None) -> list[str]:
    if not args:
        return []
    lines = []
    for current_word, next_word in itertools.pairwise(args):
        lines.append(f"For want of a {current_word} the {next_word} was lost.")
    if qualifier:
        lines.append(f"And all for the want of a {qualifier} {args[0]}.")
    else:
        lines.append(f"And all for the want of a {args[0]}.")
    return lines
