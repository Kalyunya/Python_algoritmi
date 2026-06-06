import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


def f(x):
    return x ** 2


def monte_carlo_integral(a, b, samples=100000):
    max_y = f(b)

    count = 0

    for _ in range(samples):
        x = random.uniform(a, b)
        y = random.uniform(0, max_y)

        if y <= f(x):
            count += 1

    rectangle_area = (b - a) * max_y

    return rectangle_area * count / samples


def draw_graph(a, b):
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)

    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')

    ax.set_title(f'Інтегрування f(x)=x² від {a} до {b}')

    plt.grid()
    plt.show()


if __name__ == "__main__":
    a = 0
    b = 2

    monte_result = monte_carlo_integral(a, b)

    quad_result, error = spi.quad(f, a, b)

    print("Monte-Carlo:", monte_result)
    print("Quad:", quad_result)
    print("Error estimate:", error)

    draw_graph(a, b)