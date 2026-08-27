# ALAB 351.4 - Functions, Tuples, Dictionaries, and Exceptions

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** August 27, 2026

Five Python scripts covering user-defined functions, default parameters and
return values, the Module 2 calculator refactored into functions, tuples and
dictionaries, and raising and catching exceptions.

## Files

| File | Purpose |
| --- | --- |
| `basic_functions.py` | Part 1 — defines `greet_user()`, `add_two_numbers()`, and `is_even()`, then demonstrates each one, storing returned values and using them in expressions. |
| `calc_with_functions.py` | Part 1 — the Module 2 calculator refactored so each operation is its own function, with `calculate()` dispatching to them and `try/except` handling bad input and division by zero. |
| `tuples_dicts.py` | Part 2 — builds a tuple of the twelve months and proves it is immutable, then adds to, updates, and loops over a dictionary of student grades. |
| `data_processing.py` | Part 2 — averages tuples of grades held in a dictionary of courses, handling an empty tuple without crashing. |
| `exception_demo.py` | Part 3 — raises a `ValueError` on purpose, catches it, runs a `finally` clause either way, and catches a generic `Exception`. |

## How to run

```bash
python3 basic_functions.py
python3 calc_with_functions.py
python3 tuples_dicts.py
python3 data_processing.py
python3 exception_demo.py
```

Python 3.9 or newer. No third-party packages required.

`calc_with_functions.py` asks for input; the other four run start to finish on
their own.

---

## Example output

### basic_functions.py

```
Part 1: greet_user()
--------------------
Hello, James! Welcome!
Hello! Welcome!

Part 2: add_two_numbers()
-------------------------
add_two_numbers(12, 30) returned 42
Doubling that result gives 84
Adding two returned values: 10

Part 3: is_even()
-----------------
4 is even: True
7 is even: False
10 is even, so this line runs.
```

### calc_with_functions.py

```
Calculator With Functions
=========================
Enter the first number: 12
Enter the second number: 4
Choose an operation (+, -, *, /): *
12 * 4 = 48
```

```
Calculator With Functions
=========================
Enter the first number: 9
Enter the second number: 0
Choose an operation (+, -, *, /): /
Error: division by zero is not allowed.
```

```
Calculator With Functions
=========================
Enter the first number: abc
Error: that is not a valid number.
```

### tuples_dicts.py

```
Tuples
======
There are 12 months in the tuple.
First month: January
Last month:  December

Tuples are immutable, error: 'tuple' object does not support item assignment

Dictionaries
============
Starting dictionary: {'Alice': 90, 'Brian': 82, 'Chloe': 95, 'Diego': 78}

After adding Elena:
{'Alice': 90, 'Brian': 82, 'Chloe': 95, 'Diego': 78, 'Elena': 88}

After updating Brian's grade:
Brian: 91

All students:
Alice: 90
Brian: 91
Chloe: 95
Diego: 78
Elena: 88
```

### data_processing.py

```
Course Averages
===============
The average grade for Math is 86.8
The average grade for Science is 78.5
The average grade for History is 94.7
  Warning: no grades to average.
The average grade for Art could not be calculated.
```

### exception_demo.py

```
Raising and catching ValueError
===============================
Trying 10 / 2
  Result: 5.0
  Division operation completed

Trying 7 / 0
  Error: Cannot divide by zero
  Division operation completed

Catching a generic Exception
============================
Something went wrong: invalid literal for int() with base 10: 'not a number'
The exception type was: ValueError
```
