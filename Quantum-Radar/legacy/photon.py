from constants import C, H


class Photon:
    def __init__(self, frequency, polarization="H"):
        self.frequency = frequency
        self.polarization = polarization

    @property
    def wavelength(self):
        return C / self.frequency

    @property
    def energy(self):
        return H * self.frequency

    def __str__(self):
        return (
            f"Photon\n"
            f"Frequency    : {self.frequency:.2e} Hz\n"
            f"Wavelength   : {self.wavelength:.4e} m\n"
            f"Energy       : {self.energy:.4e} J\n"
            f"Polarization : {self.polarization}"
        )