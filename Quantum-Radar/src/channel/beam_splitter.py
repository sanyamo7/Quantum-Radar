"""
Beam Splitter Model

Implements the target reflection model used in
Quantum Illumination.

Returned mode:

a_R = √κ a_S + √(1-κ) a_B
"""

from qutip import Qobj
import numpy as np


class BeamSplitter:
    """
    Beam splitter representing target reflectivity.
    """

    def __init__(self, reflectivity: float):

        if not (0 <= reflectivity <= 1):
            raise ValueError("Reflectivity must be between 0 and 1.")

        self.kappa = reflectivity

    @property
    def transmission(self):

        return 1 - self.kappa

    def matrix(self):

        k = np.sqrt(self.kappa)

        t = np.sqrt(self.transmission)

        return Qobj([
            [k, t],
            [t, -k]
        ])

    def __str__(self):

        return (
            f"BeamSplitter("
            f"reflectivity={self.kappa:.3f}, "
            f"transmission={self.transmission:.3f})"
        )