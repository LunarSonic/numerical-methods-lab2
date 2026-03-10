import numpy as np

from constants.settings import DERIVATIVE_STEP

class EquationForSystem:
    def __init__(self, f, description):
        self.f = f
        self.description = description

    def __str__(self):
        return self.description

    def get_partial_derivative(self, x_vec, i):
        h = DERIVATIVE_STEP
        x_plus = np.array(x_vec, dtype=float)
        x_minus = np.array(x_vec, dtype=float)
        x_plus[i] += h
        x_minus[i] -= h
        return (self.f(x_plus) - self.f(x_minus)) / (2 * h)