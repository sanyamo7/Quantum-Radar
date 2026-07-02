# from photon import Photon
# from constants import DEFAULT_FREQUENCY

# from quantum_states import (
#     KET_ZERO,
#     KET_ONE,
#     print_state
# )

# from quantum_gates import (
#     X,
#     H,
#     apply_gate
# )
# from entanglement import create_bell_state
# from entanglement import print_state as print_entangled_state

# def main():

#     print("=" * 60)
#     print("Quantum Radar Simulator")
#     print("=" * 60)

#     photon = Photon(DEFAULT_FREQUENCY)

#     print("\nPhoton Properties")
#     print("-----------------")
#     print(photon)

#     print_state("|0>", KET_ZERO)

#     print_state("|1>", KET_ONE)

#     # --------------------------------------------
#     # Apply X Gate
#     # --------------------------------------------

#     state = apply_gate(X, KET_ZERO)

#     print_state("X|0>", state)

#     # --------------------------------------------
#     # Apply Hadamard Gate
#     # --------------------------------------------

#     state = apply_gate(H, KET_ZERO)

#     print_state("H|0>", state)

#     bell = create_bell_state()

#     print_entangled_state(
#         "Bell State |Φ+>",
#         bell
#     )
# if __name__ == "__main__":
#     main()

from transmitter import QuantumTransmitter
from target import Target
from quantum_channel import QuantumChannel
from receiver import QuantumReceiver


def main():

    transmitter = QuantumTransmitter()

    target = Target(
        distance=1500,
        reflectivity=0.35
    )

    channel = QuantumChannel(
        loss_probability=0.15,
        noise_probability=0.05
    )

    receiver = QuantumReceiver()

    print(target)

    print("\nRunning Simulation...\n")

    for pulse in range(20):

        bell = transmitter.generate_pair()

        reflected = target.detect_reflection()

        reflected = channel.transmit(reflected)

        noise = channel.add_noise()

        detected = receiver.receive(
            reflected,
            noise
        )

        print(
            f"Pulse {pulse+1:02d} | "
            f"Reflection={reflected} | "
            f"Noise={noise} | "
            f"Detected={detected}"
        )

    print("\nSimulation Finished\n")

    print(transmitter.statistics())

    print(f"Receiver Detections : {receiver.detections}")


if __name__ == "__main__":
    main()