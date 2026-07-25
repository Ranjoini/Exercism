"""Wordy exercise."""


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
    valid_ops = {"plus", "minus", "multiplied", "divided"}

    for token in tokens:
        if token not in valid_ops:
            try:
                int(token)
            except ValueError:
                raise ValueError("unknown operation")
    if len(tokens) % 2 == 0:
        raise ValueError("syntax error")

    for i, token in enumerate(tokens):
        if i % 2 == 0:
            try:
                int(token)
            except ValueError:
                raise ValueError("syntax error")
        else:
            if token not in valid_ops:
                raise ValueError("syntax error")

    # 3. Left to right calculator
    total = int(tokens[0])

    for i in range(1, len(tokens), 2):
        op = tokens[i]
        next_num = int(tokens[i + 1])

        if op == "plus":
            total += next_num
        elif op == "minus":
            total -= next_num
        elif op == "multiplied":
            total *= next_num
        elif op == "divided":
            total /= next_num

    return int(total)
