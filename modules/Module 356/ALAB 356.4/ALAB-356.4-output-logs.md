# ALAB 356.4 — Output Logs

Full terminal transcripts for all four scripts.

## fibonacci_generator.py

```
$ python3 fibonacci_generator.py
Fibonacci #1: 0
Fibonacci #2: 1
Fibonacci #3: 1
Fibonacci #4: 2
Fibonacci #5: 3
Fibonacci #6: 5
Fibonacci #7: 8
Fibonacci #8: 13
Fibonacci #9: 21
Fibonacci #10: 34
```

`gen_fibonacci(10)` yields ten values one at a time; the loop numbers them
`#1` through `#10` as it consumes the generator.

## multiplier_closure.py

```
$ python3 multiplier_closure.py
times3(5) = 15
times3(12) = 36
times10(5) = 50
times10(7) = 70
```

`times3` and `times10` are two separate closures returned by
`make_multiplier(3)` and `make_multiplier(10)`. Each remembers its own
`factor` after `make_multiplier` has already returned.

## diary.py

Run twice, back to back, to show both branches of the `os.path.exists`
check.

**Run 1 — file does not exist yet:**

```
$ python3 diary.py
diary.txt did not exist - created it.
Enter a diary entry (blank to stop): Started the OOP lab today, feeling good about inheritance.
Enter a diary entry (blank to stop): Finished the SavingsAccount subclass, moving on to generators next.
Enter a diary entry (blank to stop):

--- diary.txt contents ---
[2026-09-13 08:45:50] Started the OOP lab today, feeling good about inheritance.
[2026-09-13 08:45:50] Finished the SavingsAccount subclass, moving on to generators next.
```

**Run 2 — file already exists, new entry appends below the old ones:**

```
$ python3 diary.py
diary.txt already exists.
Enter a diary entry (blank to stop): Second run - confirming append works and the old entries are still here.
Enter a diary entry (blank to stop):

--- diary.txt contents ---
[2026-09-13 08:45:50] Started the OOP lab today, feeling good about inheritance.
[2026-09-13 08:45:50] Finished the SavingsAccount subclass, moving on to generators next.
[2026-09-13 08:46:09] Second run - confirming append works and the old entries are still here.
```

Both entries from run 1 are still there in run 2 — `open(DIARY_FILE, "a")`
appends rather than overwrites, and the loop stops the moment an empty
line is entered.

## calendar_utility.py

Run four times: the two demonstration cases plus both error paths.

**Run 1 — the given month contains today's date:**

```
$ python3 calendar_utility.py
Enter a year: 2026
Enter a month (1-12): 9

   September 2026
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30

Today (2026-09-13) is within September 2026.
```

**Run 2 — the given month does not contain today's date:**

```
$ python3 calendar_utility.py
Enter a year: 2026
Enter a month (1-12): 12

   December 2026
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

Today (2026-09-13) is NOT within December 2026.
```

**Run 3 — month out of range:**

```
$ python3 calendar_utility.py
Enter a year: 2026
Enter a month (1-12): 13
Error: month must be between 1 and 12, got 13
```

**Run 4 — non-numeric month:**

```
$ python3 calendar_utility.py
Enter a year: 2026
Enter a month (1-12): twelve
Error: invalid literal for int() with base 10: 'twelve'
```

Runs 3 and 4 are both caught by the same `except ValueError:` block — one
comes from the explicit range check, the other from `int()` itself, the
same pattern used in ALAB 356.2's age validator.
