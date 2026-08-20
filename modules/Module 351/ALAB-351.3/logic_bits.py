# ALAB 351.3 - Part 3: Logic and Bitwise Operations (bonus)
# James Sloan
#
# Two short demonstrations: the logical operators and/or/not on boolean values
# typed by the user, and the bitwise operators on the integers 5 and 3.

# ---------------------------------------------------------------------------
# Part A: Logical operators
# input() always hands back text, so the typed answer has to be turned into a
# real True or False. .lower() lets "True", "true" and "TRUE" all work, and the
# "in" test accepts either the word or the digit 1. Anything else counts as False.
# ---------------------------------------------------------------------------
print("Logical operators")
print("=================")

first_text = input("Enter the first value (True/False or 1/0): ").strip()
second_text = input("Enter the second value (True/False or 1/0): ").strip()

first = first_text.lower() in ("true", "1")
second = second_text.lower() in ("true", "1")

print()
print(f"first  = {first}")
print(f"second = {second}")
print()

print(f"first and second = {first and second}")   # True only when BOTH are True
print(f"first or second  = {first or second}")    # True when EITHER is True
print(f"not first        = {not first}")          # flips a value to its opposite
print(f"not second       = {not second}")
print()

# ---------------------------------------------------------------------------
# Part B: Bitwise operators
# These work on the individual bits inside a number rather than on its value.
# bin() shows those bits, with the 0b in front marking a binary number.
# bin() does not pad with leading zeros, so 3 prints as 0b11 rather than 0b011.
# Lining the two up by hand shows what the comparisons below are working on:
#   5 -> 101
#   3 -> 011
# ---------------------------------------------------------------------------
print("Bitwise operators")
print("=================")

a = 5
b = 3

print(f"a = {a} -> {bin(a)}")
print(f"b = {b} -> {bin(b)}")
print()

print(f"a & b  = {a & b}  -> {bin(a & b)}")      # 1 only where BOTH have a 1
print(f"a | b  = {a | b}  -> {bin(a | b)}")      # 1 where EITHER has a 1
print(f"a ^ b  = {a ^ b}  -> {bin(a ^ b)}")      # XOR: 1 where they DIFFER
print(f"~a     = {~a} -> {bin(~a)}")             # flips every bit (see note below)
print(f"a << 1 = {a << 1} -> {bin(a << 1)}")     # shift left doubles the number
print(f"a >> 1 = {a >> 1}  -> {bin(a >> 1)}")    # shift right halves it

# Note on ~ : Python has no fixed number of bits per integer, so it prints the
# flipped result as a negative number instead of a raw row of bits. ~5 is -6.
# Note on >> : shifting right throws away the bit that falls off the end, so
# 5 >> 1 is 2 and not 2.5 - the remainder is dropped, not rounded.
