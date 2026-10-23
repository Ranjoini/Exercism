"""Robot name exercise."""

import random
import string
from typing import ClassVar


class Robot:
    used_names: ClassVar[set[str]] = set()

    def _generate_name(self):
        """Make a helper function to avoid repeating yourself in the init and reset."""
        while True:
            letters = random.choices(string.ascii_uppercase, k=2)
            digits = random.choices(string.digits, k=3)
            new_name = "".join(letters + digits)
            if new_name not in Robot.used_names:
                Robot.used_names.add(new_name)
                return new_name

    def __init__(self):
        self.name = self._generate_name()

    def reset(self):
        self.name = self._generate_name()
