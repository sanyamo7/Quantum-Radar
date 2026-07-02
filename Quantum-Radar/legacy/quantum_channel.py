"""
Quantum Channel
"""

import numpy as np


class QuantumChannel:

    def __init__(self,
                 loss_probability=0.2,
                 noise_probability=0.1):

        self.loss_probability = loss_probability
        self.noise_probability = noise_probability

    def transmit(self, photon_exists=True):

        if not photon_exists:
            return False

        # Photon Lost

        if np.random.random() < self.loss_probability:
            return False

        return True

    def add_noise(self):

        if np.random.random() < self.noise_probability:
            return True

        return False