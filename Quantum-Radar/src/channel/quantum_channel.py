"""
Quantum Channel

Combines all physical effects experienced by
the transmitted signal photon.
"""

from src.channel.loss_channel import LossChannel
from src.channel.thermal_noise import ThermalNoise
from src.channel.beam_splitter import BeamSplitter


class QuantumChannel:

    def __init__(
        self,
        eta: float,
        reflectivity: float,
        mean_photons: float,
        dimension: int = 2
    ):

        self.loss = LossChannel(eta)

        self.beam = BeamSplitter(reflectivity)

        self.noise = ThermalNoise(
            dimension=dimension,
            mean_photons=mean_photons
        )

    def propagate(self, rho):
        """
        Propagate the signal through the channel.

        Returns
        -------
        dict
            {
                "after_loss": ...,
                "thermal": ...,
                "beam": ...
            }
        """

        after_loss = self.loss.apply(rho)

        thermal = self.noise.state()

        return {
            "after_loss": after_loss,
            "thermal": thermal,
            "beam": self.beam
        }