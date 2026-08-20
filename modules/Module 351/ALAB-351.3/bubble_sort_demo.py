# ALAB 351.3 - Part 2: Bubble Sort
# James Sloan
#
# Sorts a list of integers by hand using bubble sort, printing the list after
# every pass so the progress of the sort is visible.
#
# How bubble sort works:
#   Walk along the list comparing each pair of neighbours. If the left one is
#   bigger than the right one, swap them. Doing that once carries the largest
#   remaining number all the way to the end of the list - it "bubbles up".
#   Repeat the walk and the next-largest number settles into place, and so on
#   until nothing is left out of order.

numbers = [64, 25, 12, 22, 11]
n = len(numbers)

print("Starting list:", numbers)
print()

# ---------------------------------------------------------------------------
# The OUTER loop counts the passes. Each completed pass locks one more number
# into its final position at the end of the list, and n - 1 passes are enough
# to place every number (the last one is left over and already correct).
# ---------------------------------------------------------------------------
for outer in range(n - 1):

    # -----------------------------------------------------------------------
    # The INNER loop does one walk along the list, comparing neighbours.
    #   n - 1  because we compare a pair, so we stop one short of the end -
    #          otherwise numbers[inner + 1] would run off the list.
    #   - outer  because the last `outer` numbers were settled by the earlier
    #            passes, so there is no reason to check them again.
    # -----------------------------------------------------------------------
    for inner in range(n - 1 - outer):

        # A swap happens only when the left number is bigger than the right
        # one, which means the pair is out of order.
        if numbers[inner] > numbers[inner + 1]:
            # Python swaps two values in a single line - the right-hand side
            # is worked out first, so no temporary variable is needed.
            numbers[inner], numbers[inner + 1] = numbers[inner + 1], numbers[inner]

    # Printed once per pass of the outer loop, to show the sort's progress.
    print(f"After pass {outer + 1}: {numbers}")

print()
print("Final sorted list:", numbers)
