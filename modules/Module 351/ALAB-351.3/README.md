# ALAB 351.3 - Conditionals, Loops, and Lists

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** August 20, 2026

Five Python scripts covering conditional execution, `for` and `while` loops,
list operations, a hand-written bubble sort, and logical and bitwise operators.

## Files

| File | Purpose |
| --- | --- |
| `grade_checker.py` | Part 1 — reads a numeric grade and converts it to a letter grade with an `if/elif/else` chain, then prints a pass or try-again message chosen by a conditional expression. |
| `even_sum.py` | Part 1 — sums the even numbers from 1 to 50 twice, once with a `for` loop and once with a `while` loop, and confirms both agree. |
| `list_operations.py` | Part 2 — creates a list of integers and steps through `sorted()`, `.sort()`, `.append()`, `.remove()`, and `.reverse()`, printing the list after each step. |
| `bubble_sort_demo.py` | Part 2 — sorts a list by hand with nested loops, printing the list after every pass to show the sort's progress. |
| `logic_bits.py` | Part 3 (bonus) — demonstrates `and`, `or`, `not` on two boolean inputs, then the six bitwise operators on 5 and 3 shown in binary with `bin()`. |

## How to run

```bash
python3 grade_checker.py
python3 even_sum.py
python3 list_operations.py
python3 bubble_sort_demo.py
python3 logic_bits.py
```

Python 3.9 or newer. No third-party packages required.

`grade_checker.py` and `logic_bits.py` ask for input; the other three run start
to finish on their own.

---

## Example output

### grade_checker.py

```
Enter a numeric grade (0-100): 85
Your grade is: B
Congratulations, you passed!
```

```
Enter a numeric grade (0-100): 55
Your grade is: F
Keep studying and try again.
```

### even_sum.py

```
Using a for loop:
The sum of even numbers from 1 to 50 is 650.

Using a while loop:
The sum of even numbers from 1 to 50 is 650.

Both loops produced the same result: True
```

### list_operations.py

```
Original list: [42, 7, 19, 3, 25]

Sorted copy from sorted(): [3, 7, 19, 25, 42]
Original list, still unchanged: [42, 7, 19, 3, 25]

After numbers.sort(), sorted in place: [3, 7, 19, 25, 42]

After appending 50: [3, 7, 19, 25, 42, 50]

After removing the value 19: [3, 7, 25, 42, 50]

After reversing: [50, 42, 25, 7, 3]
```

### bubble_sort_demo.py

```
Starting list: [64, 25, 12, 22, 11]

After pass 1: [25, 12, 22, 11, 64]
After pass 2: [12, 22, 11, 25, 64]
After pass 3: [12, 11, 22, 25, 64]
After pass 4: [11, 12, 22, 25, 64]

Final sorted list: [11, 12, 22, 25, 64]
```

### logic_bits.py

```
Logical operators
=================
Enter the first value (True/False or 1/0): True
Enter the second value (True/False or 1/0): False

first  = True
second = False

first and second = False
first or second  = True
not first        = False
not second       = True

Bitwise operators
=================
a = 5 -> 0b101
b = 3 -> 0b11

a & b  = 1  -> 0b1
a | b  = 7  -> 0b111
a ^ b  = 6  -> 0b110
~a     = -6 -> -0b110
a << 1 = 10 -> 0b1010
a >> 1 = 2  -> 0b10
```
