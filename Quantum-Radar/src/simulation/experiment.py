"""
Quantum Illumination Experiment

Coordinates all modules of the simulator.
"""

from qutip import basis, ket2dm

from src.quantum.photon_pair import PhotonPair
from src.quantum.quantum_memory import QuantumMemory

from src.channel.quantum_channel import QuantumChannel

from src.radar.target import Target


class QuantumRadarExperiment:

    """
    Runs one complete quantum radar experiment.
    """

    def __init__(
        self,
        eta=0.8,
        reflectivity=0.1,
        mean_photons=0.2,
        distance=1000,
    ):

        self.memory = QuantumMemory()

        self.channel = QuantumChannel(
            eta=eta,
            reflectivity=reflectivity,
            mean_photons=mean_photons
        )

        self.target = Target(
            distance=distance,
            reflectivity=reflectivity
        )

    def run(self):

        # Generate Bell Pair
        pair = PhotonPair()

        # Split pair
        signal = pair.signal()

        idler = pair.idler()

        # Store idler
        self.memory.store(idler)

        # Example transmitted state |1><1|
        signal_density = ket2dm(basis(2, 1))

        # Pass through channel
        channel_output = self.channel.propagate(signal_density)

        return {

            "signal": signal,

            "idler": idler,

            "channel": channel_output,

            "target": self.target

        }