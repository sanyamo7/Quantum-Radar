"""
Radar Target
"""


class Target:

    def __init__(
        self,
        distance: float,
        reflectivity: float
    ):

        self.distance = distance

        self.reflectivity = reflectivity

    def path_loss(self):

        return 1 / (self.distance ** 2)

    def effective_reflectivity(self):

        return self.reflectivity * self.path_loss()

    def __str__(self):

        return (
            f"Target(\n"
            f" distance={self.distance} m,\n"
            f" reflectivity={self.reflectivity},\n"
            f" effective={self.effective_reflectivity():.6e}\n)"
        )