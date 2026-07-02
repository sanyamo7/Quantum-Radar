"""
Photon Pair Module

Creates the Signal and Idler photons
from an entangled Bell pair.
"""

from qutip import bell_state, ptrace


class PhotonPair:

    def __init__(self):

        self.state = bell_state("00")

    def signal(self):
        """
        Returns the signal photon
        """
        return ptrace(self.state, 0)

    def idler(self):
        """
        Returns the idler photon
        """
        return ptrace(self.state, 1)

    def full_state(self):
        """
        Returns the complete Bell pair.
        """
        return self.state