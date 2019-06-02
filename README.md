[![Build status](https://travis-ci.org/marcoradic/QCpy.svg?branch=master)](https://travis-ci.org/marcoradic)

# qc.py - A Quantum Computer Simulator in Python

Simplistic Simulator for a Quantum Computer using the gate-based model. 
Supports several standard and parametrized single qubit gates and measurements in the standard basis.

## Example usage
```python
test_circuit = Circuit(3)
test_circuit.add_layer([gates.hadamard, gates.identity, gates.identity])
test_circuit.add_layer([gates.identity, gates.identity, gates.identity])
test_circuit.build_unitary()
test_circuit.run()
```

Output:
```
Running Circuit
Circuit._apply_unitary took 0.00027895s
== measurement probabilities ==
|000> 0.50000
|001> 0.00000
|010> 0.00000
|011> 0.00000
|100> 0.50000
|101> 0.00000
|110> 0.00000
|111> 0.00000
```

More info on Quantum Computers: [Nielsen and Chuang - Quantum Computation and Quantum Information](https://www.cambridge.org/core/books/quantum-computation-and-quantum-information/01E10196D0A682A6AEFFEA52D53BE9AE)

