# Entanglement module for quantum radar simulator

import numpy as np

from quantum_states import KET_ZERO
from quantum_gates import H, CNOT, apply_gate


def tensor_product(state1, state2):
    """
    Compute the tensor (Kronecker) product of two quantum states.
    """
    return np.kron(state1, state2)


def create_zero_zero():
    """
    Create the two-qubit |00> state.
    """
    return tensor_product(KET_ZERO, KET_ZERO)


def create_bell_state():
    """
    Create the Bell state |Φ+> = (|00> + |11>) / sqrt(2)
    """

    # Step 1: |00>
    state = create_zero_zero()

    # Step 2: Apply Hadamard to the first qubit
    H1 = np.kron(H, np.eye(2))

    state = apply_gate(H1, state)

    # Step 3: Apply CNOT
    state = apply_gate(CNOT, state)

    return state


def print_state(name, state):

    print(f"\n{name}")
    print("-" * len(name))
    print(state)
    print(f"\nShape : {state.shape}")
    print(f"Norm  : {np.linalg.norm(state):.4f}")