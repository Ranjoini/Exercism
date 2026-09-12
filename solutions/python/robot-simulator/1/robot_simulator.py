NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3


class Robot:
    from typing import ClassVar

    ADVANCE_MAP: ClassVar[dict[int, tuple[int, int]]] = {
        NORTH: (0, 1),
        EAST: (1, 0),
        SOUTH: (0, -1),
        WEST: (-1, 0),
    }

    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.direction = direction
        self.x = x_pos
        self.y = y_pos
        self.INSTRUCTION_MAP = {
            "R": self._turn_right,
            "L": self._turn_left,
            "A": self._advance,
        }

    @property
    def coordinates(self) -> tuple[int, int]:
        return (self.x, self.y)

    def _turn_right(self) -> None:
        self.direction = (self.direction + 1) % 4

    def _turn_left(self) -> None:
        self.direction = (self.direction - 1) % 4

    def _advance(self) -> None:
        dx, dy = self.ADVANCE_MAP[self.direction]
        self.x += dx
        self.y += dy

    def move(self, instructions: str) -> None:
        for command in instructions:
            action = self.INSTRUCTION_MAP.get(command)
            if action:
                action()
