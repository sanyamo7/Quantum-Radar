"""
Thermal Noise Channel

Models a thermal environment using QuTiP.
"""

from qutip import thermal_dm


class ThermalNoise:
    """
    Creates thermal states with a given average photon number.
    """

    def __init__(self, dimension: int = 2, mean_photons: float = 0.1):
        if dimension < 2:
            raise ValueError("dimension must be >= 2")

        if mean_photons < 0:
            raise ValueError("mean_photons must be >= 0")

        self.dimension = dimension
        self.mean_photons = mean_photons

    def state(self):
        """
        Returns the thermal density matrix.
        """
        return thermal_dm(self.dimension, self.mean_photons)