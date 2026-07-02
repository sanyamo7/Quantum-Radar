from qutip import bell_state

from density_matrix import create_density_matrix

psi = bell_state("00")

rho = create_density_matrix(psi)

print("Bell State")
print(psi)

print()

print("Density Matrix")
print(rho)