"""Space age."""


class SpaceAge:
    EARTH_YEAR_SECONDS = 31557600

    def __init__(self, seconds):
        """Pre-calculate the earth_years."""
        self.seconds = seconds
        # 1. Pre-calculate the Earth years immediately upon creation
        self.earth_years = self.seconds / self.EARTH_YEAR_SECONDS

    # 2. Our single, DRY math engine
    def _calculate(self, orbital_period):
        """Do all the conversion math here so that we don't have to repeat ourselves."""
        return round(self.earth_years / orbital_period, 2)

    # 3. The public methods become beautiful one-liners
    def on_earth(self):
        return self._calculate(1.0)

    def on_mercury(self):
        return self._calculate(0.2408467)

    def on_venus(self):
        return self._calculate(0.61519726)

    def on_mars(self):
        return self._calculate(1.8808158)

    def on_jupiter(self):
        return self._calculate(11.862615)

    def on_saturn(self):
        return self._calculate(29.447498)

    def on_uranus(self):
        return self._calculate(84.016846)

    def on_neptune(self):
        return self._calculate(164.79132)
