# ALAB 351.2 - Part 1: Data Types, Variables, and Operators
# James Sloan

# ---------------------------------------------------------------------------
# Section 1: Variable declarations
# Each variable holds a different data type:
#   str   - text, written in quotes
#   int   - a whole number, no decimal point
#   float - a number with a decimal point
# ---------------------------------------------------------------------------
name = "James"      # str
age = 41            # int
height = 1.83       # float, measured in meters

print("Section 1: Variables and their data types")
print("-----------------------------------------")

# type(x).__name__ prints the type as plain text ("str") instead of "<class 'str'>".
print(f"name   = {name!r}  -> {type(name).__name__}")
print(f"age    = {age}      -> {type(age).__name__}")
print(f"height = {height}    -> {type(height).__name__}")
print()

# ---------------------------------------------------------------------------
# Section 2: Introduction sentence
# An f-string drops each variable straight into the sentence inside {}.
# The :.2f formats the float to exactly two decimal places.
# ---------------------------------------------------------------------------
print("Section 2: Introduction")
print("-----------------------")
print(f"Hi, my name is {name}. I am {age} years old and {height:.2f} meters tall.")
print()

# ---------------------------------------------------------------------------
# Section 3: Age in 5 years
# The + operator on two ints does ordinary addition.
# ---------------------------------------------------------------------------
print("Section 3: Age in five years")
print("----------------------------")
years_ahead = 5
future_age = age + years_ahead          # addition
print(f"In {years_ahead} years I will be {future_age} years old.")
print()

# ---------------------------------------------------------------------------
# Section 4: Area of a rectangle (5.5 x 2)
# The * operator multiplies. length is a float and width is an int, so Python
# promotes the result to a float automatically.
# ---------------------------------------------------------------------------
print("Section 4: Rectangle area")
print("-------------------------")
length = 5.5        # float
width = 2           # int
area = length * width                   # multiplication
print(f"A rectangle {length} x {width} has an area of {area:.2f} square units.")
print()

# ---------------------------------------------------------------------------
# Section 5: More operators
# Arithmetic operators demonstrated here:
#   +  addition          -  subtraction      *  multiplication
#   /  true division     // floor division   %  remainder (modulo)
#   ** exponent
# String operators demonstrated here:
#   +  concatenation (joins strings)
#   *  repetition (repeats a string)
#   .upper() / .lower() / len()  string methods and the built-in length function
# ---------------------------------------------------------------------------
print("Section 5: Operators")
print("--------------------")

# Arithmetic
print(f"age + 5     = {age + 5}")                 # addition
print(f"age - 5     = {age - 5}")                 # subtraction
print(f"age * 2     = {age * 2}")                 # multiplication
print(f"age / 2     = {age / 2}")                 # true division always gives a float
print(f"age // 2    = {age // 2}")                # floor division throws away the remainder
print(f"age % 2     = {age % 2}")                 # remainder: 1 means the number is odd
print(f"height ** 2 = {height ** 2:.4f}")         # exponent

# Strings
first_name = "James"
last_name = "Sloan"
full_name = first_name + " " + last_name          # concatenation with +
print(f'"{first_name}" + " " + "{last_name}" = "{full_name}"')
print(f'"-" * 20 = "{"-" * 20}"')                 # repetition with *
print(f'"{full_name}".upper() = "{full_name.upper()}"')
print(f'len("{full_name}") = {len(full_name)}')
