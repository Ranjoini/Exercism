import secrets
from itertools import cycle
from string import ascii_lowercase as ALPHABET


class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = "".join(secrets.choice(ALPHABET) for _ in range(100))
        else:
            self.key = key

    def _engine(self, text, direction):
        """Create a helper function, since both encode and decode are almost the same."""
        result = []
        for text_char, key_char in zip(text, cycle(self.key)):
            result.append(
                ALPHABET[(ord(text_char) % 97 + (ord(key_char) % 97 * direction)) % 26]
            )
        return "".join(result)

    def encode(self, text):
        """Translate to cipher."""
        # Call enigne in normal mode
        return self._engine(text, direction=1)

    def decode(self, text):
        """Translate to normal."""
        # Put it in reverse
        return self._engine(text, direction=-1)
