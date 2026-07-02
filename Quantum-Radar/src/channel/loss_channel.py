"""
Amplitude Damping Channel

Models photon loss in free-space propagation.
"""

from qutip import Qobj, kraus_to_super
import numpy as np


class LossChannel:

    def __init__(self, eta: float):
        """
        Parameters
        ----------
        eta : float
            Transmission efficiency (0 ≤ eta ≤ 1)

            eta = 1.0 → perfect channel
            eta = 0.0 → complete loss
        """

        if not (0 <= eta <= 1):
            raise ValueError("eta must be between 0 and 1.")

        self.eta = eta

    def kraus_operators(self):

        K0 = Qobj([
            [1, 0],
            [0, np.sqrt(self.eta)]
        ])

        K1 = Qobj([
            [0, np.sqrt(1 - self.eta)],
            [0, 0]
        ])

        return [K0, K1]

    def superoperator(self):
        return kraus_to_super(self.kraus_operators())

    def apply(self, rho):

        result = 0

        for K in self.kraus_operators():
            result += K * rho * K.dag()

        return result