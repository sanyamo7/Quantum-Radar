"""
Quantum Transmitter
Generates entangled photon pairs for the radar.
"""

from entanglement import create_bell_state


class QuantumTransmitter:

    def __init__(self):
        self.total_pairs_generated = 0

    def generate_pair(self):
        """
        Generate one entangled Bell pair.
        """

        self.total_pairs_generated += 1

        bell_state = create_bell_state()

        return bell_state

    def statistics(self):

        return {
            "Generated Pairs": self.total_pairs_generated
        }