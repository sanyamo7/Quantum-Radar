"""
Radar Transmitter
"""

import sys
import os

# Allow imports from src/quantum
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "quantum"))

from photon_pair import PhotonPair
from quantum_memory import QuantumMemory


class RadarTransmitter:

    def __init__(self):

        self.memory = QuantumMemory()

    def transmit(self):

        pair = PhotonPair()

        signal = pair.signal()

        idler = pair.idler()

        self.memory.store(idler)

        return signal

    def stored_idler(self):

        return self.memory.retrieve()