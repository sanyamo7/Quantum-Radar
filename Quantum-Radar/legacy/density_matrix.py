# Density Matrix Utilities


from qutip import ket2dm


def create_density_matrix(state):
    """
    Convert a ket vector into a density matrix.
    """
    return ket2dm(state)