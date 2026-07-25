"""Code for the matching brackets exercise."""


def is_paired(input_string: str) -> bool:
    """Determine whether opening and closing brackets are properly paired within the input text."""
    stack = []
    reference_manual = {")": "(", "]": "[", "}": "{"}
    for char in input_string:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if len(stack) == 0:
                return False
            last_opened = stack.pop()
            expected_opener = reference_manual[char]
            if last_opened != expected_opener:
                return False
    return len(stack) == 0
