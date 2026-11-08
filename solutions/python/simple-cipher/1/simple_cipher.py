import secrets
import string
from typing import ClassVar


class Cipher:
    ALPHABET: ClassVar[str] = string.ascii_lowercase

    def __init__(self, key=None):
        if key is None:
            self.key = "".join(secrets.choice(self.ALPHABET) for _ in range(100))
        else:
            self.key = key

    def _engine(self, text, direction):
        """Create a helper function, since both encode and decode are almost the same."""
        result = []
        for text_index, text_char in enumerate(text):
            # Wrap around the key if text is longer than key
            key_char = self.key[text_index % len(self.key)]
            text_value = self.ALPHABET.index(text_char)
            shift_value = self.ALPHABET.index(key_char)
            # This is where we do the shift when encoding and decoding
            new_index = (text_value + (shift_value * direction)) % 26
            result.append(self.ALPHABET[new_index])
        return "".join(result)

    def encode(self, text):
        """Translate to cipher."""
        # Call enigne in normal mode
        return self._engine(text, direction=1)

    def decode(self, text):
        """Translate to normal."""
        # Put it in reverse
        return self._engine(text, direction=-1)
