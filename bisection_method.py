

import numpy as np
from colors import bcolors

def find_roots_np(a, b, c, d, e):
    # Define the function
    def f(x):
        return 5 * x**6 - 3 * x**5 - 4 * x**2 - 2

    # Generate a range of x values
    x_values = np.linspace(-100, 100, 10000)

    # Evaluate the function at each x value
    y_values = f(x_values)

    # Find where the sign of the y values change
    sign_changes = np.where(np.diff(np.sign(y_values)))[0]

    # Iterate over the sign changes and refine the root using bisection method
    for idx in sign_changes:
        root = np.round(bisection_method(f, x_values[idx], x_values[idx+1]), 6)
        print(bcolors.OKBLUE, "Root:", root, bcolors.ENDC)

def bisection_method(f, a, b, tol=1e-6):
    """
    Implements the bisection method to find roots of the equation f(x) = 0 within a specified range.

    Args:
    f (function): The function for which roots are to be found.
    a (float): Lower bound of the search range.
    b (float): Upper bound of the search range.
    tol (float): Tolerance (stop when |b - a| < tol).

    Returns:
    float: Approximation of the root.
    """
    while (b - a) >= tol:
        # Find midpoint
        c = (a + b) / 2.0

        # Check if midpoint is root
        if f(c) == 0.0:
            return c

        # Decide the side to repeat the steps
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2.0


