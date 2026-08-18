# ALAB 351.2 — Data Types, Variables, Operators, and Basic I/O

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** August 18, 2026

Three Python scripts covering data types, variables, arithmetic and string
operators, and user input/output.

## Files

| File | Purpose |
| --- | --- |
| `types_and_vars.py` | Part 1 — declares typed variables, prints an introduction, calculates a future age and a rectangle area, and demonstrates arithmetic and string operators. |
| `simple_calculator.py` | Part 2 — reads two numbers and an operator from the user, performs the calculation with an if/elif/else chain, and prints a friendly result. Invalid input is re-prompted rather than crashing. |
| `string_fun.py` | Bonus — reads a word and reports its length, uppercase form, and three repetitions, plus a few extras. |

## How to run

```bash
python3 types_and_vars.py
python3 simple_calculator.py
python3 string_fun.py
```

Python 3.9 or newer. No third-party packages required.

---

## Example output

### `types_and_vars.py`

This script takes no input, so it produces the same output every run.

```
Section 1: Variables and their data types
-----------------------------------------
name   = 'James'  -> str
age    = 41      -> int
height = 1.83    -> float

Section 2: Introduction
-----------------------
Hello, my name is James. I am 41 years old and 1.83 meters tall.

Section 3: Age in five years
----------------------------
In 5 years, I will be 46 years old.

Section 4: Rectangle area
-------------------------
The area of a 5.5 x 2 rectangle is 11.0.

Section 5: Operators
--------------------
age + 5     = 46
age - 5     = 36
age * 2     = 82
age / 2     = 20.5
age // 2    = 20
age % 2     = 1
height ** 2 = 3.3489
"James" + " " + "Sloan" = "James Sloan"
"-" * 20 = "--------------------"
"James Sloan".upper() = "JAMES SLOAN"
len("James Sloan") = 11
```

### `simple_calculator.py`

**Multiplication — the format required by the lab:**

```
Simple Calculator
=================
Enter the first number: 7
Enter the second number: 3
Choose an operation (+, -, *, /): *

7 * 3 = 21
```

**Decimals and negatives:**

```
Simple Calculator
=================
Enter the first number: -12
Enter the second number: 4.25
Choose an operation (+, -, *, /): +

-12 + 4.25 = -7.75
```

**Long decimal result — rounded to four places so it stays readable:**

```
Simple Calculator
=================
Enter the first number: 10
Enter the second number: 3
Choose an operation (+, -, *, /): /

10 / 3 = 3.3333
```

**Invalid number, then an invalid operator — the program re-asks instead of crashing:**

```
Simple Calculator
=================
Enter the first number: abc
  'abc' is not a number. Please try again.
Enter the first number: 15.5
Enter the second number: 4
Choose an operation (+, -, *, /): ^
  '^' is not one of +, -, *, /. Please try again.
Choose an operation (+, -, *, /): -

15.5 - 4 = 11.5
```

**Division by zero:**

```
Simple Calculator
=================
Enter the first number: 8
Enter the second number: 0
Choose an operation (+, -, *, /): /

8 / 0 = undefined
Error: division by zero is not allowed.
```

### `string_fun.py`

```
String Fun
==========
Enter a word: Python

Length:        6 characters
Uppercase:     PYTHON
Repeated x3:   Python Python Python
Lowercase:     python
Title case:    Python
First letter:  P
Last letter:   n
Reversed:      nohtyP
Palindrome:    no
```

**A palindrome:**

```
String Fun
==========
Enter a word: racecar

Length:        7 characters
Uppercase:     RACECAR
Repeated x3:   racecar racecar racecar
Lowercase:     racecar
Title case:    Racecar
First letter:  r
Last letter:   r
Reversed:      racecar
Palindrome:    yes, 'racecar' reads the same backwards
```

**Empty input — falls back to a default word:**

```
String Fun
==========
Enter a word:
(No word entered - using 'Python' instead.)

Length:        6 characters
Uppercase:     PYTHON
Repeated x3:   Python Python Python
...
```
