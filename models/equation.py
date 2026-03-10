import numpy as np

from constants.settings import GRID_POINTS

class Equation:
    def __init__(self, f, f_derivative, f_double_derivative, description):
        self.f = f
        self.f_derivative = f_derivative
        self.f_double_derivative = f_double_derivative
        self.description = description

    def __str__(self):
        return self.description

    def is_single_root_exist(self, a, b):
        if self.f(a) * self.f(b) > 0:
            return False
        points = np.linspace(a, b, GRID_POINTS)
        derivatives = [self.f_derivative(x) for x in points]
        if max(derivatives) * min(derivatives) < 0:
            return False
        return True