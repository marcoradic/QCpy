import numpy as np

class Circuit(object):

    def __init__(self):
        self.gates = dict()
        had = Gate(np.array([[1,1], [1,-1]]))
        self.gates.append(had)