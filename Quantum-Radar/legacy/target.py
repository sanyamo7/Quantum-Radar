"""
Target Model
"""

import numpy as np


class Target:

    def __init__(self,
                 distance=1000,
                 reflectivity=0.3):

        self.distance = distance
        self.reflectivity = reflectivity

    def detect_reflection(self):

        probability = self.reflectivity

        if np.random.random() < probability:
            return True

        return False

    def __str__(self):

        return (
            f"Target\n"
            f"Distance : {self.distance} m\n"
            f"Reflectivity : {self.reflectivity}"
        )