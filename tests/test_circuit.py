from qcpy.circuit import Circuit
from qcpy import gates
from qcpy import utils

import math

import pytest
import numpy as np

@pytest.fixture
def single_qubit_circuit():
    """ Returns a single qubit Circuit in ground state"""
    return Circuit(1)

@pytest.fixture
def two_qubit_circuit():
    """ Returns a 2-qubit Circuit in ground state"""
    return Circuit(2)

@pytest.fixture
def three_qubit_circuit():
    """ Returns a 3-qubit Circuit in ground state"""
    return Circuit(3)

def test_ground_state_single_qubit(single_qubit_circuit):
    np.testing.assert_equal(single_qubit_circuit.state, np.array([1, 0]))

def test_identity_unitary_two_qubit(two_qubit_circuit):
    ground_state = two_qubit_circuit.state
    two_qubit_circuit.add_layer([gates.identity, gates.identity])
    two_qubit_circuit.build_unitary()
    two_qubit_circuit.run()
    np.testing.assert_equal(two_qubit_circuit.state, ground_state)

def test_equal_superposition_three_qubits(three_qubit_circuit):
    three_qubit_circuit.add_layer([gates.hadamard, gates.hadamard, gates.hadamard])
    three_qubit_circuit.build_unitary()
    three_qubit_circuit.run()
    equal_superosition_state = utils.tensor(3 * [np.array([1/math.sqrt(2), 1/math.sqrt(2)])])
    np.testing.assert_almost_equal(three_qubit_circuit.state, equal_superosition_state)
