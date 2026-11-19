import math


def cipher_text(plain_text):
    """Change the plaintext into grid format."""
    # Safety check
    if not plain_text:
        return ""
    # Filtering the text into the string format required, used isalnum. to ensure both letters and numbers are kept
    formated_str = "".join(char.lower() for char in plain_text if char.isalnum())
    if not formated_str:
        return ""
    # Translating Quadratic formula into code
    length = len(formated_str)
    c = math.ceil(math.sqrt(length))
    r = math.ceil(length / c) if c > 0 else 0
    ecoded_chunkc = [formated_str[i::c].ljust(r) for i in range(c)]
    return " ".join(ecoded_chunkc)
