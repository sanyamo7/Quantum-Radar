from qutip import basis, ket2dm

from src.channel.loss_channel import LossChannel

# |1>
state = basis(2, 1)

rho = ket2dm(state)

channel = LossChannel(eta=0.7)

rho_after = channel.apply(rho)

print("Original Density Matrix\n")
print(rho)

print("\nAfter Channel\n")
print(rho_after)