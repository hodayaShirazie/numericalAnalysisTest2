import math
import numpy as np
from colors import bcolors


import math
#
# class bcolors:
#     OKBLUE = '\033[94m'
#     ENDC = '\033[0m'

def iterative_method(f, x0, lower_bound, upper_bound, tol=1e-6):
    """
    Implements the fixed-point iteration method to find roots of the equation f(x) = 0 within a specified range.

    Args:
    f (function): The function for which roots are to be found.
    x0 (float): Initial guess.
    lower_bound (float): Lower bound of the search range.
    upper_bound (float): Upper bound of the search range.
    tol (float): Tolerance (stop when |x_{n+1} - x_{n}| < tol).

    Returns:
    float: Approximation of the root.
    int: Number of iterations performed.
    """
    # print(f"Iterating with x0 = {x0} within range [{lower_bound}, {upper_bound}]")
    # print("Iter    xr        g(xr)      xr+1")
    xr = x0
    for n in range(100):  # Iterating for 10 times
        g_xr = f(xr)
        xr_plus_1 = g_xr + xr

        # print(f"{n+1:<5}   {xr:<10.6f} {g_xr:<10.6f} {xr_plus_1:<10.6f}")  # Printing iteration
        if abs(xr_plus_1 - xr) < tol:
            return xr_plus_1, n

        xr = xr_plus_1
        if xr_plus_1 < lower_bound or xr_plus_1 > upper_bound:
            # print("Root is outside the specified range.")
            return None, -1

    # print("Series did not converge within the specified range.")
    return None, -1  # Return -1 to indicate non-convergence



def find_roots_iterative_method(a, b, c, d, e):
    f = lambda x: 5 * x**6 - 3 * x**5 - 4 * x**2 - 2

    for i in range(-1000, 1000, 1):
        initial_guess = i
        root, iterations = iterative_method(f, initial_guess, -100, 100)
        if root is not None:
            print(bcolors.OKBLUE, "Root:", root, bcolors.ENDC)
