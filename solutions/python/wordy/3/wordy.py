"""Wordy exercise."""

import operator


def answer(question: str) -> int:
    """Execute math operations based on the question asked."""
    # 1. String Sanitizer
    if not question.startswith("What is") or not question.endswith("?"):
        raise ValueError("unknown operation")
    clean_text = question.removeprefix("What is").removesuffix("?")
    clean_text = clean_text.replace("multiplied by", "multiplied")
    clean_text = clean_text.replace("divided by", "divided")

    tokens = clean_text.split()
    if not tokens:
        raise ValueError("syntax error")

    # 2. Ze-Bouncer
    OPS = {
        "plus": operator.add,
        "minus": operator.sub,
        "multiplied": operator.mul,
        "divided": operator.truediv,
    }
    # Scan for unknown operations
    for token in tokens:
        if token not in OPS:
            try:
                int(token)
            except ValueError as err:
                raise ValueError("unknown operation") from err
    # Enforce alternating pattern[ num, op, num, op, num]
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            try:
                int(token)
            except ValueError as err:
                raise ValueError("syntax error") from err
        else:
            if token not in OPS:
                raise ValueError("syntax error")

    # 3. Left to right calculator
    total = int(tokens[0])

    for i in range(1, len(tokens), 2):
        op_word = tokens[i]
        next_num = int(tokens[i + 1])

        total = OPS[op_word](total, next_num)

    return int(total)
