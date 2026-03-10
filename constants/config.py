import numpy as np

from models.equation import Equation
from models.system_of_equations import SystemOfEquations
from models.equation_for_system import EquationForSystem

EQUATIONS = [
    Equation(
        lambda x: x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76,
        lambda x: 3 * x ** 2 - 3.78 * x - 2,
        lambda x: 6 * x - 3.78,
        "x^3 - 1.89x^2 - 2x + 1.76 = 0"
    ),
    Equation(
        lambda x: np.sin(x) - 0.5,
        lambda x: np.cos(x),
        lambda x: -np.sin(x),
        "sin(x) - 0.5 = 0"
    ),
    Equation(
        lambda x: x * np.exp(x) - 2,
        lambda x: np.exp(x) * (x + 1),
        lambda x: np.exp(x) * (x + 2),
        "x*e^x - 2 = 0"
    ),
    Equation(
        lambda x: np.cos(x) + 0.5 * x - 1,
        lambda x: -np.sin(x) + 0.5,
        lambda x: -np.cos(x),
        "cos(x) + 0.5x - 1 = 0"
    ),
    Equation(
        lambda x: x ** 3 - x + 4,
        lambda x: 3 * x ** 2 - 1,
        lambda x: 6 * x,
        "x^3 - x + 4 = 0"
    )
]

SYSTEMS = [
    SystemOfEquations([
        EquationForSystem(lambda x: x[0] ** 2 + x[1] ** 2 - 4, "x^2 + y^2 = 4"),
        EquationForSystem(lambda x: x[1] - 3 * x[0] ** 2, "y = 3x^2")
    ], "Система: окружность и парабола"),

    SystemOfEquations([
        EquationForSystem(lambda x: np.tan(x[0] * x[1] + 0.3) - x[0] ** 2, "tg(xy + 0.3) = x^2"),
        EquationForSystem(lambda x: 0.5 * x[0] ** 2 + 2 * x[1] ** 2 - 1, "0.5x^2 + 2y^2 = 1")
    ], "Система: тангенс и эллипс"),

    SystemOfEquations([
        EquationForSystem(lambda x: np.sin(x[0]) - x[1] + 1, "sin(x) - y = -1"),
        EquationForSystem(lambda x: x[0] + np.cos(x[1] - 1) - 0.5, "x + cos(y-1) = 0.5")
    ], "Система: синус и косинус"),

    SystemOfEquations([
        EquationForSystem(lambda x: 0.1 * x[0]**2 + x[0] + 0.2 * x[1]**2 - 0.3, "0.1x^2 + x + 0.2y^2 = 0.3"),
        EquationForSystem(lambda x: 0.2 * x[0]**2 + x[1] + 0.1 * x[0] * x[1] - 0.7, "0.2x^2 + y + 0.1xy = 0.7")
    ], "Система: эллипс и парабола")
]

EQ_METHODS = ["Метод хорд", "Метод Ньютона", "Метод простых итераций"]
SYS_METHODS = ["Метод Ньютона"]