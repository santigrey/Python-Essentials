# ALAB 351.4 - Part 1: Calculator Refactored With Functions
# James Sloan
#
# The Module 2 calculator rebuilt so each operation is its own function.
# calculate() picks the right one, and try/except handles bad input and
# division by zero.


# ---------------------------------------------------------------------------
# One function per operation. Each takes two numbers and returns the result.
#
# divide() does not check for a zero divisor itself. Dividing by zero raises
# ZeroDivisionError, and letting that error travel back to the caller is the
# point of Part 1 - the main program catches it instead.
# ---------------------------------------------------------------------------
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# ---------------------------------------------------------------------------
# calculate() is a function that calls other functions.
#
# Parameters: a and b are the numbers, op is the operation symbol.
# Returns: the result of the matching operation, or an error message string
# if op is not one of the four symbols.
#
# The if/elif chain matches the symbol and hands the work to the right
# function above. Only one branch can run, and each one returns immediately.
# ---------------------------------------------------------------------------
def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return f"Error: '{op}' is not a valid operation."


# ---------------------------------------------------------------------------
# tidy() keeps the printing readable.
# float() turns every input into a float, so 7 comes back as 7.0. If the
# number is really whole, print the int version so the line reads 21, not 21.0.
# ---------------------------------------------------------------------------
def tidy(number):
    return int(number) if number == int(number) else round(number, 4)


# ---------------------------------------------------------------------------
# Main program.
# ---------------------------------------------------------------------------
print("Calculator With Functions")
print("=========================")

# try/except around the input conversion. float() raises ValueError when the
# text is not a number, so both numbers are read inside the same try block.
try:
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
except ValueError:
    print("Error: that is not a valid number.")
else:
    operation = input("Choose an operation (+, -, *, /): ").strip()

    # try/except around the calculation itself, which is where dividing by
    # zero fails.
    try:
        result = calculate(first, second, operation)
    except ZeroDivisionError:
        print("Error: division by zero is not allowed.")
    else:
        # An invalid symbol makes calculate() return a message instead of a
        # number, so check the type before formatting it as an equation.
        if isinstance(result, str):
            print(result)
        else:
            print(f"{tidy(first)} {operation} {tidy(second)} = {tidy(result)}")
