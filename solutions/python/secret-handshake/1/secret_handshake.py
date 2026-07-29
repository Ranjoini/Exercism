"""Secret handshake."""

ACTIONS = ["wink", "double blink", "close your eyes", "jump"]


def commands(binary_str: str) -> list:
    """Return the action given the binary string."""
    reverse_binary = binary_str[::-1]
    actions = []
    for index, digit in enumerate(reverse_binary[:4]):
        if digit == "1":
            actions.append(ACTIONS[index])
    if reverse_binary[4] == "1":
        actions.reverse()
    return actions
