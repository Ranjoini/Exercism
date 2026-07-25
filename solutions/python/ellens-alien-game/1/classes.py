"""Solution to Ellen's Alien Game exercise."""


class Alien:
    total_aliens_created = 0

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        """Evaluate the x_coordinate and y_coordinate of alien."""
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    def hit(self):
        """Relay the damage of the alien based on whether it is hit."""
        if self.health > 0:
            self.health -= 1

    def is_alive(self) -> bool:
        """Evaluate the state of the alien based on health."""
        return self.health > 0

    def teleport(self, new_x_coordinate: int, new_y_coordinate: int) -> None:
        """Instantly flash new positional coordinates onto this instance's tracking matrix."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other) -> None:
        """Execute a collision protocol if this unit overlaps with another object."""
        if (
            self.x_coordinate == other.x_coordinate
            and self.y_coordinate == other.y_coordinate
        ):
            self.hit()


def new_aliens_collection(positions: list[tuple[int, int]]) -> list[Alien]:
    """Generate a deployed fleet array of live alien instances from a layout manifest."""
    return [Alien(x, y) for x, y in positions]
