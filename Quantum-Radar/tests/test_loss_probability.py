from qutip import basis, ket2dm

from src.channel.loss_channel import LossChannel

etas = [1.0, 0.8, 0.5, 0.2, 0.0]

rho = ket2dm(basis(2, 1))

for eta in etas:

    channel = LossChannel(eta)

    result = channel.apply(rho)

    print("=" * 50)
    print(f"η = {eta}")
    print(result)