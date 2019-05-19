import numpy as np

from functools import reduce

def normalize(self, vector):
    return vector / np.linalg.norm(vector)

def tensor(tensor_items):
    return reduce(lambda x, y: np.kron(x, y), tensor_items)

def matmul(matrices):
    return reduce(lambda x, y: x @ y, matrices)