# ALAB 351.3 - Part 2: List Operations
# James Sloan
#
# Creates a list of integers and walks through the common list operations,
# printing the list after each step so the change is visible.

# ---------------------------------------------------------------------------
# Step 1: Create the list and print it.
# A list is written in square brackets with the items separated by commas.
# ---------------------------------------------------------------------------
numbers = [42, 7, 19, 3, 25]
print("Original list:", numbers)
print()

# ---------------------------------------------------------------------------
# Step 2: sorted() is a built-in function that hands back a NEW sorted list
# and leaves the original alone. Printing the original again afterwards is
# what proves it was not changed.
# ---------------------------------------------------------------------------
print("Sorted copy from sorted():", sorted(numbers))
print("Original list, still unchanged:", numbers)
print()

# ---------------------------------------------------------------------------
# Step 3: .sort() is a list method that sorts the list in place. It changes
# the list itself and hands back nothing. That is the key difference from
# sorted() in Step 2.
# ---------------------------------------------------------------------------
numbers.sort()
print("After numbers.sort(), sorted in place:", numbers)
print()

# ---------------------------------------------------------------------------
# Step 4: .append() adds one item onto the end of the list.
# ---------------------------------------------------------------------------
numbers.append(50)
print("After appending 50:", numbers)
print()

# ---------------------------------------------------------------------------
# Step 5: .remove() deletes the first item matching the value given.
# Removing by position would be numbers.pop(0) instead, which removes by index.
# ---------------------------------------------------------------------------
numbers.remove(19)
print("After removing the value 19:", numbers)
print()

# ---------------------------------------------------------------------------
# Step 6: .reverse() flips the order of the list in place.
# ---------------------------------------------------------------------------
numbers.reverse()
print("After reversing:", numbers)
