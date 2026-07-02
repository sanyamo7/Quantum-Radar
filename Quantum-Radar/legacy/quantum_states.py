
#Quantum basis states and helper functions.


import numpy as np

# --------------------------------------------------
# Computational Basis States
# --------------------------------------------------

KET_ZERO = np.array([[1],
                     [0]], dtype=complex)

KET_ONE = np.array([[0],
                    [1]], dtype=complex)


# --------------------------------------------------
# Utility Functions
# --------------------------------------------------

def normalize(state):
    """
    Normalize a quantum state.
    """

    norm = np.linalg.norm(state)

    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")

    return state / norm


def print_state(name, state):
    """
    Pretty print a quantum state.
    """

    print(f"\n{name}")

    print("-" * len(name))

    print(state)

    print(f"\nDimension : {state.shape}")

    print(f"Norm      : {np.linalg.norm(state):.4f}")