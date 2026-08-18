# ALAB 351.2 - Part 2: Simple Calculator
# James Sloan
#
# Asks for two numbers and an operation, then prints the result.
# Bad input never crashes the program - it just asks again.

print("Simple Calculator")
print("=================")

# ---------------------------------------------------------------------------
# Step 1: Read the first number.
# input() always hands back a string, so float() converts it to a number.
# If the text is not a number, float() raises a ValueError. The try/except
# catches that, prints a message, and the while loop asks again.
# ---------------------------------------------------------------------------
while True:
    first_text = input("Enter the first number: ").strip()
    try:
        first = float(first_text)
        break                                   # valid number, leave the loop
    except ValueError:
        print(f"  '{first_text}' is not a number. Please try again.")

# ---------------------------------------------------------------------------
# Step 2: Read the second number the same way.
# ---------------------------------------------------------------------------
while True:
    second_text = input("Enter the second number: ").strip()
    try:
        second = float(second_text)
        break
    except ValueError:
        print(f"  '{second_text}' is not a number. Please try again.")

# ---------------------------------------------------------------------------
# Step 3: Read the operation and check it against the four allowed symbols.
# ---------------------------------------------------------------------------
while True:
    operation = input("Choose an operation (+, -, *, /): ").strip()
    if operation in ("+", "-", "*", "/"):
        break
    print(f"  '{operation}' is not one of +, -, *, /. Please try again.")

# ---------------------------------------------------------------------------
# Step 4: Do the math with an if/elif/else chain.
# division_by_zero is a flag so the message below knows dividing failed.
# ---------------------------------------------------------------------------
division_by_zero = False

if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
else:                                           # the only symbol left is "/"
    if second == 0:
        division_by_zero = True                 # dividing by zero is undefined
        result = None
    else:
        result = first / second

# ---------------------------------------------------------------------------
# Step 5: Print the result in a friendly "7 * 3 = 21" format.
# float() turns every input into a float, so 7 comes back as 7.0. Comparing a
# number to int(number) tells me whether it is really a whole number, and if it
# is I print the int version so the line reads 21 instead of 21.0.
# ---------------------------------------------------------------------------
first_display = int(first) if first == int(first) else first
second_display = int(second) if second == int(second) else second

print()
if division_by_zero:
    print(f"{first_display} / {second_display} = undefined")
    print("Error: division by zero is not allowed.")
else:
    # round() keeps long decimals such as 10 / 3 readable.
    result = round(result, 4)
    result_display = int(result) if result == int(result) else result
    print(f"{first_display} {operation} {second_display} = {result_display}")
