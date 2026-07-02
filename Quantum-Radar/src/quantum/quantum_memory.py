"""
Quantum Memory

Stores the idler photon until
the reflected signal arrives.
"""


class QuantumMemory:

    def __init__(self):

        self.memory = None

    def store(self, idler):

        self.memory = idler

    def retrieve(self):

        return self.memory

    def clear(self):

        self.memory = None

    def is_empty(self):

        return self.memory is None