import numpy as np
i = np.complex(0, 1)

identity = np.eye(2)
hadamard = 1/np.sqrt(2) * np.array([[1,1], [1,-1]])
pauli_x = np.array([[0, 1], [1, 0]])
pauli_y = np.array([[0, -i], [i, 0]])
pauli_z = np.array([[1, 0], [0, -1]])

def rot_x(angle):
    return identity

def rot_y(angle):
    return identity

def rot_z(angle):
    return identity