from qutip import basis, ket2dm

from src.channel.quantum_channel import QuantumChannel

# Create |1>
signal = ket2dm(basis(2, 1))

channel = QuantumChannel(
    eta=0.8,
    reflectivity=0.1,
    mean_photons=0.2
)

result = channel.propagate(signal)

print("\nSignal After Loss\n")
print(result["after_loss"])

print("\nThermal State\n")
print(result["thermal"])

print("\nBeam Splitter\n")
print(result["beam"])