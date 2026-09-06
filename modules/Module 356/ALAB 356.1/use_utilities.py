# ALAB 356.1 - Task 2: Importing the custom module from the package.
# Run this file from the ALAB 356.1 folder so Python can find mypackage.

from mypackage import utilities

print("greet():")
print(utilities.greet("James"))

print()
print("factorial():")
print("5! =", utilities.factorial(5))
print("7! =", utilities.factorial(7))
