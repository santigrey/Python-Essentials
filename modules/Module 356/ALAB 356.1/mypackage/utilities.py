# ALAB 356.1 - Task 2: Custom module inside the mypackage package.
# Defines greet() and factorial() for use_utilities.py to import.

import math


def greet(name):
    """Return a greeting string for the given name."""
    return "Hello, " + name + "! Welcome to Python modules."


def factorial(n):
    """Return the factorial of n using the math module."""
    return math.factorial(n)
