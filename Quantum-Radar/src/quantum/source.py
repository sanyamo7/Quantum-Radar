"""
Quantum Source

Generates entangled Bell pairs.
"""

from qutip import bell_state


class QuantumSource:

    def __init__(self):

        self.generated_pairs = 0

    def generate(self):

        self.generated_pairs += 1

        return bell_state("00")