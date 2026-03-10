import numpy as np

from models.result import Result
from constants.settings import MAX_ITERATIONS, GRID_POINTS, DERIVATIVE_STEP

def chord_method(equation, a, b, epsilon):
    f = equation.f
    if f(a) * f(b) > 0:
        raise Exception("На выбранном интервале нет корня или их четное количество, то есть функция не меняет знак")
    f2 = equation.f_double_derivative
    log = []
    iterations = 0
    if f(a) * f2(a) > 0:
        c = a
        x = b
    else:
        c = b
        x = a
    while iterations < MAX_ITERATIONS:
        iterations += 1
        x_prev = x
        x = x_prev - f(x_prev) * (x_prev - c) / (f(x_prev) - f(c))
        delta = abs(x - x_prev)
        log.append({
            "№ шага": iterations,
            'a': a,
            'x': x,
            'f(a)': f(a),
            'f(x)': f(x),
            'delta': delta
        })
        if delta <= epsilon:
            return Result(x, iterations, log, f(x))
    raise Exception(f"Произведено {MAX_ITERATIONS} итераций, решение не было найдено")

def newton_method(equation, a, b, epsilon):
    f = equation.f
    df = equation.f_derivative
    f2 = equation.f_double_derivative
    log = []
    iterations = 0

    if f(a) * f2(a) > 0:
        x = a
    elif f(b) * f2(b) > 0:
        x = b
    else:
        raise Exception("Не удалось выбрать начальное приближение")
    while iterations < MAX_ITERATIONS:
        iterations += 1
        x_prev = x
        if abs(df(x_prev)) < 1e-12:
            raise Exception("Производная равна 0")
        x = x_prev - f(x_prev)/df(x_prev)
        delta = abs(x - x_prev)
        log.append({
            "№ шага": iterations,
            "x_k": x_prev,
            "f(x_k)": f(x_prev),
            "f'(x_k)": df(x_prev),
            "x_{k+1}": x,
            "f(x_{k+1})": f(x),
            "f'(x_{k+1})": df(x),
            "delta": delta
        })
        if delta <= epsilon:
            return Result(x, iterations, log, f(x))
    raise Exception(f"Произведено {MAX_ITERATIONS} итераций, решение не было найдено")

def simple_iteration_method(equation, a, b, epsilon):
    f = equation.f
    df = equation.f_derivative
    log = []
    iterations = 0

    max_derivative = max(abs(df(a)), abs(df(b)))
    if max_derivative < 1e-12:
        raise Exception("Производная равна 0")
    _lambda = 1/max_derivative
    if df(a) > 0:
        _lambda *= -1
    phi = lambda x: x + _lambda * f(x)

    xs = np.linspace(a, b, GRID_POINTS)
    phi_derivatives = []
    for x_val in xs:
        d_phi = abs((phi(x_val + DERIVATIVE_STEP) - phi(x_val - DERIVATIVE_STEP)) / (2 * DERIVATIVE_STEP))
        phi_derivatives.append(d_phi)
    q = max(phi_derivatives)
    if q >= 1:
        raise Exception("Метод не сходится, так как q >= 1")
    x_prev = a
    while iterations < MAX_ITERATIONS:
        iterations += 1
        x = phi(x_prev)
        delta = abs(x - x_prev)
        log.append({
            "№ шага": iterations,
            "x_k": x_prev,
            'x_{k+1}': x,
            'phi(x_{k+1})': phi(x),
            'f(x_{k+1})': f(x),
            'delta': delta
        })
        if delta <= epsilon:
            return Result(x, iterations, log, f(x))
        x_prev = x
    raise Exception(f"Произведено {MAX_ITERATIONS} итераций, решение не было найдено")