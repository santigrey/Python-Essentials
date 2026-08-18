# ALAB 351.2 — Data Types, Variables, Operators, and Basic I/O

**James Sloan** · UCI 3052 Python Essentials · Module 351 · August 18, 2026

---

## Repository

**Repository:** [github.com/santigrey/Python-Essentials](https://github.com/santigrey/Python-Essentials)

**Lab folder:** [modules/Module 351/ALAB-351.2](https://github.com/santigrey/Python-Essentials/tree/main/modules/Module%20351/ALAB-351.2)

All three scripts and a README containing example output are in that folder.

| File | Task |
| --- | --- |
| `types_and_vars.py` | Part 1 — variables, data types, operators |
| `simple_calculator.py` | Part 2 — two-number calculator |
| `string_fun.py` | Bonus — string operations |
| `README.md` | Example output from running each script |

---

## Example Output

### `types_and_vars.py`

Takes no input, so the output is the same every run.

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

Full transcript of one run:

```
Simple Calculator
=================
Enter the first number: 7
Enter the second number: 3
Choose an operation (+, -, *, /): *

7 * 3 = 21
```

The other three operations, run the same way:

| First | Second | Operation | Output |
| --- | --- | --- | --- |
| `15.5` | `4` | `-` | `15.5 - 4 = 11.5` |
| `-12` | `4.25` | `+` | `-12 + 4.25 = -7.75` |
| `10` | `3` | `/` | `10 / 3 = 3.3333` |

Invalid input is re-prompted instead of crashing, and division by zero is caught:

```
Enter the first number: abc
  'abc' is not a number. Please try again.
Enter the first number: 8
Enter the second number: 0
Choose an operation (+, -, *, /): /

8 / 0 = undefined
Error: division by zero is not allowed.
```

### `string_fun.py`

```
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
