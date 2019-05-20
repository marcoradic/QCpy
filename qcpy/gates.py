import numpy as np
import cmath
from cmath import sin, cos

i = np.complex(0, 1)

# single qubit gates
identity = np.eye(2)
hadamard = 1 / np.sqrt(2) * np.array([[1, 1], [1, -1]])
pauli_x = np.array([[0, 1], [1, 0]])
pauli_y = np.array([[0, -i], [i, 0]])
pauli_z = np.array([[1, 0], [0, -1]])
phase_s = np.array([[1, 0], [0, i]])
pi_8 = np.array([[1, 0], [0, cmath.exp(i*(cmath.pi/4))]])


def rot_x(angle):
    """Rotation operator around x-axis
    
    Arguments:
        angle {float} -- rotation angle
    
    Returns:
        np.array -- rotation_x operator
    """
    return np.array(
        [
            [cos(angle / 2.0), -i * sin(angle / 2.0)],
            [-i * sin(angle / 2.0), cos(angle / 2.0)],
        ]
    )


def rot_y(angle):
    """Rotation operator around y-axis
    
    Arguments:
        angle {float} -- rotation angle
    
    Returns:
        np.array -- rotation_x operator
    """
    return np.array(
        [
            [cos(angle / 2.0), -sin(angle / 2.0)],
            [sin(angle / 2.0), cos(angle / 2.0)],
        ]
    )


def rot_z(angle):
    """Rotation operator around z-axis
    
    Arguments:
        angle {float} -- rotation angle
    
    Returns:
        np.array -- rotation_x operator
    """
    return np.array(
        [
            [cmath.exp(-i * (angle / 2.0)), 0],
            [0, cmath.exp(i * (angle / 2.0))],
        ]
    )

