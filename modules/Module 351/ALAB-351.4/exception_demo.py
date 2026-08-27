# ALAB 351.4 - Part 3: Exception Handling
# James Sloan
#
# Raises an exception on purpose, catches it, and shows that a finally clause
# runs either way. Also catches a generic Exception.


# ---------------------------------------------------------------------------
# safe_divide() divides a by b.
#
# Parameters: a is the numerator, b is the divisor.
# Returns: a / b when b is not zero.
# Raises: ValueError when b is zero.
#
# "raise" creates the error myself instead of waiting for Python to do it.
# The message in the parentheses is what the except block can print later.
# ---------------------------------------------------------------------------
def safe_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


print("Raising and catching ValueError")
print("===============================")

# Two test pairs - the second one has a zero divisor, so it fails.
test_values = [(10, 2), (7, 0)]

for a, b in test_values:
    print(f"Trying {a} / {b}")
    try:
        answer = safe_divide(a, b)
        print(f"  Result: {answer}")
    except ValueError as error:
        # "as error" gives me the exception object so I can print its message.
        print(f"  Error: {error}")
    finally:
        # finally always runs - after a success and after a caught error.
        print("  Division operation completed")
    print()


# ---------------------------------------------------------------------------
# Catching a generic Exception.
#
# int() raises ValueError on text that is not a number. Catching Exception
# instead of ValueError works because ValueError is a kind of Exception, so a
# generic catch picks up anything the block might throw.
# ---------------------------------------------------------------------------
print("Catching a generic Exception")
print("============================")

try:
    number = int("not a number")
    print(f"Converted value: {number}")
except Exception as error:
    print(f"Something went wrong: {error}")
    print(f"The exception type was: {type(error).__name__}")
