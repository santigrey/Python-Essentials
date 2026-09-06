# ALAB 356.1 - Task 1: Using Built-in Modules
# Imports math, random, and platform. Picks a random number, floors its
# square root, and reports the operating system and Python version.

import math
import random
import platform

# random.randint(1, 100) includes both 1 and 100.
number = random.randint(1, 100)

# math.sqrt returns a float; math.floor rounds it down to a whole number.
root = math.sqrt(number)
floored_root = math.floor(root)

print("Random Number:", number)
print("Square Root (floored):", floored_root)
print("Operating System:", platform.system())
print("Python Version:", platform.python_version())
