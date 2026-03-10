import numpy as np

from numpy.linalg import LinAlgError
from models.result import Result
from constants.settings import MAX_ITERATIONS

def newton_method_for_system(system, x_0, epsilon):
    x = np.array(x_0, dtype=float)
    log = []
    iterations = 0
    while iterations < MAX_ITERATIONS:
        iterations += 1
        jacobian = system.get_jacobian(x)
        f_values = system.get_value(x)
        try:
            dx = np.linalg.solve(jacobian, -f_values)
        except LinAlgError:
            raise Exception("Матрица Якоби вырождена => промежуточная система не имеет решений")
        x_next = x + dx
        error_vector = np.abs(x_next - x)
        max_diff = np.max(error_vector)
        log.append({
            "№ шага": iterations,
            "x_k": x[0],
            "y_k": x[1],
            "x_{k+1}": x_next[0],
            "y_{k+1}": x_next[1],
            "|dx|": dx[0],
            "|dy|": dx[1],
            "max|dx|": max_diff
        })
        if max_diff <= epsilon:
            return Result(x_next, iterations, log)
        x = x_next
    raise Exception(f"Произведено {MAX_ITERATIONS} итераций, решение не было найдено")



