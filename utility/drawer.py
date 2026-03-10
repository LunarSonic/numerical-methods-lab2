import numpy as np

from matplotlib import pyplot as plt
from constants.settings import LOG_DECIMALS

def draw_equation(result_x, left, right, equation):
    side_step = abs(right-left) * 0.2
    l, r = left - side_step, right + side_step
    x = np.linspace(l, r, 1000)
    y = [equation.f(val) for val in x]
    plt.plot(x, y, label=f"f(x)", color="blue", linewidth=2)
    y_root = equation.f(result_x)
    plt.scatter([result_x], [y_root], color="pink", s=100, zorder=5, label=f"Корень: ({round(result_x, LOG_DECIMALS)})")
    plt.vlines([left, right], plt.gca().get_ylim()[0], [equation.f(left), equation.f(right)],
               colors="gray", linestyles="--", alpha=0.5, label="Границы [a, b]")
    plt.axhline(0, color="black", linewidth=1)
    plt.title(f"График: {equation.description}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.legend()
    plt.show()

def draw_system(result_vec, initial_vec, system):
    if system.n > 2:
        return
    dist_root = np.sqrt(result_vec[0]**2 + result_vec[1]**2)
    dist_init = np.sqrt(initial_vec[0]**2 + initial_vec[1]**2)
    r = max(dist_root, dist_init, 1) * 1.5
    plt.figure(figsize=(8, 6))
    x = np.linspace(-r, r, 1000)
    y = np.linspace(-r, r, 1000)
    X, Y = np.meshgrid(x, y)
    Z1 = np.array([[system.equations[0].f([xi, yi]) for xi in x] for yi in y])
    Z2 = np.array([[system.equations[1].f([xi, yi]) for xi in x] for yi in y])

    plt.contour(X, Y, Z1, levels=[0], colors="blue", linewidths=2)
    plt.contour(X, Y, Z2, levels=[0], colors="green", linewidths=2)
    plt.scatter([initial_vec[0]], [initial_vec[1]], color="pink", s=80, label="Начальная точка")
    plt.scatter([result_vec[0]], [result_vec[1]], color="red", marker="x", s=120, label="Найденный корень")
    plt.axhline(0, color="black", alpha=0.5)
    plt.axvline(0, color="black", alpha=0.5)
    plt.title(f"Система: {system.description}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()