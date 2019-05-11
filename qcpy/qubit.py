import numpy as np

class Qubit(object):

    def __init__(self, amplitudes):
        self.amplitudes = amplitudes

    def _validate(self):
        pass

    def normalize(self):
        pass

    def __mul__(self, other):
        """Tensor Product
        
        Arguments:
            other {Qubit} -- Qubit to perform tensor product with
        
        Returns:
            Vector -- resulting vector
        """
        return np.kron(self.amplitudes, other.amplitudes)
