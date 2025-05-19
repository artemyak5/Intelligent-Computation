import numpy as np

# Fitness functions for GA optimization problems

def branin(ind):
    """
    Branin function
    Global minima: ~0.397887 at (x, y) = (-pi, 12.275), (pi, 2.275), (9.42478, 2.475)
    Domain: x in [-5, 10], y in [0, 15]
    """
    x, y = ind[0], ind[1]
    a = 1.0
    b = 5.1 / (4 * np.pi**2)
    c = 5.0 / np.pi
    r = 6.0
    s = 10.0
    t = 1.0 / (8 * np.pi)
    return a * (y - b * x**2 + c * x - r)**2 + s * (1 - t) * np.cos(x) + s


def easom(ind):
    """
    Easom function
    Global minimum: -1 at (pi, pi)
    Domain: x, y in [-100, 100]
    """
    x, y = ind[0], ind[1]
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))


def goldstein_price(ind):
    """
    Goldstein-Price function
    Global minimum: 3 at (0, -1)
    Domain: x, y in [-2, 2]
    """
    x, y = ind[0], ind[1]
    term1 = (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)
    term2 = (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2)
    return term1 + term2


def six_hump_camel(ind):
    """
    Six-Hump Camel function
    Global minima: approximately -1.0316 at (+/-0.0898, +/-0.7126)
    Domain: x in [-3, 3], y in [-2, 2]
    """
    x, y = ind[0], ind[1]
    return (4 - 2.1*x**2 + (x**4)/3) * x**2 + x*y + (-4 + 4*y**2) * y**2


# Dictionary of available fitness functions and their search domains
FUNCTIONS = {
    "branin": {
        "func": branin,
        "bounds": [(-5.0, 10.0), (0.0, 15.0)]
    },
    "easom": {
        "func": easom,
        "bounds": [(-100.0, 100.0), (-100.0, 100.0)]
    },
    "goldstein_price": {
        "func": goldstein_price,
        "bounds": [(-2.0, 2.0), (-2.0, 2.0)]
    },
    "six_hump_camel": {
        "func": six_hump_camel,
        "bounds": [(-3.0, 3.0), (-2.0, 2.0)]
    }
}
