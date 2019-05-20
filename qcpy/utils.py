import numpy as np

from functools import reduce

def normalize(self, vector):
    return vector / np.linalg.norm(vector)

def tensor(tensor_items):
    return reduce(lambda x, y: np.kron(x, y), tensor_items)

def matmul(matrices):
    return reduce(lambda x, y: x @ y, matrices)

def timer(f):
    """
    Decorator function that times the execution time of a decorated function
    """

    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        print('{0} took {1:.8f}s'.format(f.__qualname__, time.time()-start))
        return result
    return wrapper