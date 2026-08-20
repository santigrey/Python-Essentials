# ALAB 351.3 - Part 1: Sum of Even Numbers
# James Sloan
#
# Adds up every even number from 1 to 50, first with a for loop and then
# with a while loop, to confirm both approaches give the same answer.

# ---------------------------------------------------------------------------
# Version 1: for loop
# range(1, 51) counts 1 through 50. The stop value is not included, so it has
# to be 51 to reach 50.
# A number is even when dividing it by 2 leaves no remainder, so the test is
# number % 2 == 0.
# ---------------------------------------------------------------------------
for_total = 0
for number in range(1, 51):
    if number % 2 == 0:
        for_total = for_total + number

print("Using a for loop:")
print(f"The sum of even numbers from 1 to 50 is {for_total}.")
print()

# ---------------------------------------------------------------------------
# Version 2: while loop
# A while loop does not count for us. We start the counter at 1, test it at
# the top of every pass, and move it forward by hand at the bottom. Leaving
# out that last step is what causes a loop to run forever.
# ---------------------------------------------------------------------------
while_total = 0
number = 1
while number <= 50:
    if number % 2 == 0:
        while_total = while_total + number
    number = number + 1

print("Using a while loop:")
print(f"The sum of even numbers from 1 to 50 is {while_total}.")
print()

# ---------------------------------------------------------------------------
# Do both versions agree?
# Yes - both print 650.
#
# The for loop is the clearer of the two for me. range() handles the starting
# value, the stop value, and the counting all on one line, so there is less to
# keep track of and no way to forget to move the counter forward. The while
# loop needs three separate pieces - start the counter, test it, increase it -
# and the answer only comes out right if all three agree with each other.
# ---------------------------------------------------------------------------
print(f"Both loops produced the same result: {for_total == while_total}")
