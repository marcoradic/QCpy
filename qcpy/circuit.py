import numpy as np

import math, cmath
from collections.abc import Iterable

import utils
import gates


class Circuit(object):
    def __init__(self, num_qubits):
        self.layers = list()
        if num_qubits <= 0:
            raise ValueError("Number of qubits must be greater 0")
        self.num_qubits = num_qubits
        self._initialize_state()
        self.unitary = None

    def _initialize_state(self):
        """ 
            Initialize the state as a zero-qubit-vector consisting of num_qubits qubits
        """
        self.state = utils.tensor(self.num_qubits * [np.array([1, 0])])

    def add_layer(self, layer):
        if isinstance(layer, Iterable):
            # TODO the following check only holds for single qubits operations, gates need to be assigned cardinalities
            if len(layer) == self.num_qubits:
                self.layers.append(layer)
            else:
                raise ValueError(
                    "number of operators for layer does not match number of qubits"
                )
        else:
            raise ValueError("provided layer argument is not iterable")

    def apply_layer(self):
        pass

    def run(self, shots=1):
        print('Running Circuit')
        self._apply_unitary()
        self._print_results()

    @utils.timer
    def _apply_unitary(self):
        self.state = self.unitary @ self.state

    def _print_results(self):
        probabilities = np.power(self.state, 2)
        maxlength_binary = len(bin(len(probabilities)-1)) -2
        leading_zero_pad_args = ''.join(['0', str(maxlength_binary), 'b'])
        print('== measurement results ==')
        for i, p in enumerate(probabilities):
            binary_repr = format(i, leading_zero_pad_args)
            print(f"|{binary_repr}> {p:.5f}")

    def build_unitary(self):
        """ 
            Builds target unitary of quantum circuit based on the added layers
        """
        self.unitary = utils.matmul(
            [utils.tensor(layer) for layer in self.layers[::-1]]
        )

    def print_unitary(self):
        print('Unitary of circuit:')
        print(self.unitary)

    def __repr__(self):
        self.print_unitary()

    def __str__(self):
        self.print_unitary()


if __name__ == "__main__":
    test_circuit = Circuit(3)
    #test_circuit.add_layer([gates.pauli_x])
    test_circuit.add_layer([gates.hadamard, gates.identity, gates.identity])
    test_circuit.build_unitary()
    #test_circuit.print_unitary()
    test_circuit.run()
    # print(utils.tensor([gates.identity, gates.hadamard]))
