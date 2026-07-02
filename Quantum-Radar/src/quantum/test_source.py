from source import QuantumSource
from density import DensityMatrix

source = QuantumSource()

psi = source.generate()

rho = DensityMatrix.create(psi)

print()

print("Bell State")

print(psi)

print()

print("Density Matrix")

print(rho)