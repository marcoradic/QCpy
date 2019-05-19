import numpy as np

import math, cmath
from collections.abc import Iterable

import utils
import gates

class Circuit(object):

    def __init__(self, num_qubits):
        self.layers = list()
        if num_qubits <= 0:
            raise ValueError('Number of qubits must be greater 0')
        self.num_qubits = num_qubits
        self.state = self._initialize_state()
        self.hamiltonian = None
    
    def _initialize_state(self):
        return utils.tensor(self.num_qubits * [np.array([1, 0])])

    def add_layer(self, layer):
        if isinstance(layer, Iterable):
            # TODO the following check only holds for single qubits operations, gates need to be assigned cardinalities
            if len(layer) == self.num_qubits:
                self.layers.append(layer)
            else:
                raise ValueError('number of operators for layer does not match number of qubits')
        else:
            raise ValueError('provided layer argument is not iterable')

    def apply_layer(self):
        pass

    def build_hamiltonian(self):
        self.hamiltonian = utils.matmul([utils.tensor(layer) for layer in self.layers[::-1]])

    def print_unitary(self):
        pass
        

if __name__ == '__main__':
    test_circuit = Circuit(1)
    print(test_circuit.state)
    test_circuit.add_layer([gates.hadamard])
    test_circuit.add_layer([gates.pauli_x])
    test_circuit.build_hamiltonian()
    print(test_circuit.hamiltonian)
    #print(utils.tensor([gates.identity, gates.hadamard]))