import numpy as np

class SystemOfEquations:
    def __init__(self, equations, description):
        self.equations = equations
        self.n = len(equations)
        self.description = description

    def __str__(self):
        return "\n".join([eq.description for eq in self.equations])

    def get_value(self, x):
        v = []
        for equation in self.equations:
            v.append(equation.f(x))
        return np.array(v)

    def get_jacobian(self, x_vec):
        jacobian = []
        for equation in self.equations:
            row = [equation.get_partial_derivative(x_vec, j) for j in range(self.n)]
            jacobian.append(row)
        return np.array(jacobian)