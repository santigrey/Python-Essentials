# ALAB 351.4 - Part 1: Writing and Using Functions
# James Sloan
#
# Defines three small functions and demonstrates each one.


# ---------------------------------------------------------------------------
# greet_user() prints a greeting for the name it is given.
#
# name is a parameter with a default value of "". Giving it a default is what
# lets me call greet_user() with no argument at all - Python fills in the ""
# for me. An empty string is falsy, so "if name" is False when nothing was
# passed and the shorter greeting runs instead.
#
# This function prints; it has no return statement, so it hands back None.
# ---------------------------------------------------------------------------
def greet_user(name=""):
    if name:
        print(f"Hello, {name}! Welcome!")
    else:
        print("Hello! Welcome!")


# ---------------------------------------------------------------------------
# add_two_numbers() takes two numbers and returns their sum.
#
# Parameters: a and b, the two numbers to add.
# Returns: the sum. "return" hands the value back to whoever called the
# function, which means the answer can be stored in a variable or used inside
# a bigger expression.
# ---------------------------------------------------------------------------
def add_two_numbers(a, b):
    return a + b


# ---------------------------------------------------------------------------
# is_even() reports whether a number is even.
#
# Parameter: num, the number to test.
# Returns: True if num is even, False if it is not.
# num % 2 is the remainder after dividing by 2. That remainder is 0 for even
# numbers, so "num % 2 == 0" is already True or False - I can return the
# comparison directly instead of writing an if/else that returns True or False.
# ---------------------------------------------------------------------------
def is_even(num):
    return num % 2 == 0


# ---------------------------------------------------------------------------
# Main part of the script - everything below here is outside the functions.
# ---------------------------------------------------------------------------
print("Part 1: greet_user()")
print("--------------------")
greet_user("James")          # with a name
greet_user()                 # without a name, so the default "" is used
print()

print("Part 2: add_two_numbers()")
print("-------------------------")
# Storing the returned value in a variable.
total = add_two_numbers(12, 30)
print(f"add_two_numbers(12, 30) returned {total}")

# Using the returned value inside a larger expression.
print(f"Doubling that result gives {total * 2}")
print(f"Adding two returned values: {add_two_numbers(1, 2) + add_two_numbers(3, 4)}")
print()

print("Part 3: is_even()")
print("-----------------")
even_check = is_even(4)
odd_check = is_even(7)
print(f"4 is even: {even_check}")
print(f"7 is even: {odd_check}")

# The returned value is a real boolean, so it can drive an if statement.
if is_even(10):
    print("10 is even, so this line runs.")
