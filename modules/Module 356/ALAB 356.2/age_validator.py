# ALAB 356.2 - Task 3: Custom Exception Test (Age Validator)
# validate_age() raises a ValueError for any age outside 0 to 120, and the
# script below catches it instead of letting the program crash.


def validate_age(age):
    """Raise a ValueError unless age is between 0 and 120 inclusive."""
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120. You entered " + str(age) + ".")
    return age


try:
    # int() also raises a ValueError if the text is not a whole number,
    # so the same except block covers both problems.
    entered_age = int(input("Enter your age: "))
    validate_age(entered_age)
except ValueError as error:
    print("Error:", error)
else:
    print("Age accepted:", entered_age)
