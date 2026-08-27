# ALAB 351.4 - Part 2: Tuples and Dictionaries
# James Sloan
#
# Shows that a tuple cannot be changed, then builds a dictionary and adds to,
# updates, and loops over it.


# ---------------------------------------------------------------------------
# A tuple is written with parentheses. Once it exists it cannot be changed.
# ---------------------------------------------------------------------------
months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print("Tuples")
print("======")
print(f"There are {len(months)} months in the tuple.")

# Index 0 is the first item. Index -1 counts back from the end, so it is the
# last item without needing to know the length.
print(f"First month: {months[0]}")
print(f"Last month:  {months[-1]}")
print()

# ---------------------------------------------------------------------------
# Trying to change a tuple raises TypeError. Wrapping it in try/except lets
# the script show the error and keep running instead of crashing.
# ---------------------------------------------------------------------------
try:
    months[0] = "NewMonth"
except TypeError as error:
    print(f"Tuples are immutable, error: {error}")
print()


# ---------------------------------------------------------------------------
# A dictionary stores key/value pairs. Here the key is a student name and the
# value is that student's grade.
# ---------------------------------------------------------------------------
students = {
    "Alice": 90,
    "Brian": 82,
    "Chloe": 95,
    "Diego": 78,
}

print("Dictionaries")
print("============")
print(f"Starting dictionary: {students}")
print()

# Assigning to a key that does not exist yet adds a new pair.
students["Elena"] = 88
print("After adding Elena:")
print(students)
print()

# Assigning to a key that already exists replaces its value instead.
students["Brian"] = 91
print("After updating Brian's grade:")
print(f"Brian: {students['Brian']}")
print()

# ---------------------------------------------------------------------------
# .items() hands back both the key and the value on each pass, so the loop
# variables name and grade are filled in together.
# ---------------------------------------------------------------------------
print("All students:")
for name, grade in students.items():
    print(f"{name}: {grade}")
