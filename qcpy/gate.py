import numpy as np

class Gate(object):

    def __init__(self, calculation_matrix):
        self.calculation_matrix = calculation_matrix

    def apply(self, vec):
        return self.calculation_matrix @ vec