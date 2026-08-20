# ALAB 351.3 - Part 1: Conditional Execution
# James Sloan
#
# Asks for a numeric grade and converts it to a letter grade.

grade = float(input("Enter a numeric grade (0-100): "))

# ---------------------------------------------------------------------------
# The if/elif/else chain is checked from the top down, so each branch only
# needs its lower bound. A grade of 95 matches "grade >= 90" and Python stops
# checking there. That top-down order is also what makes the edge cases work:
# 100 lands in A, 90 lands in A, 60 lands in D, and 0 falls through to F.
# ---------------------------------------------------------------------------
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your grade is: {letter}")

# A conditional expression picks one of two values on a single line:
#   <value if true> if <condition> else <value if false>
# A, B and C are the passing grades; D and F are not.
passed = letter in ("A", "B", "C")
congrats = "Congratulations, you passed!"
encourage = "Keep studying and try again."

message = congrats if passed else encourage
print(message)
