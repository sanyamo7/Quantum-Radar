"""
Density Matrix Utilities
"""

from qutip import ket2dm


class DensityMatrix:

    @staticmethod
    def create(state):

        return ket2dm(state)