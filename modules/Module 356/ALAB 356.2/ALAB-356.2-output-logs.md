# ALAB 356.2 — Output Logs

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** September 6, 2026

Text logs showing that each script works as intended, satisfying the submission
requirement: *"Include sample outputs (screenshots or text logs) showing that
each script works as intended."*

Every block below is a captured terminal transcript — the typed input is echoed
exactly as it appeared on screen, and nothing here is retyped by hand.

**Environment:** macOS (`Darwin`), Python 3.13.2. No third-party packages.

---

## Task 1 — `string_manipulation.py`

```
Enter a sentence: Hello World from Python Essentials
Uppercase: HELLO WORLD FROM PYTHON ESSENTIALS
Reversed: slaitnessE nohtyP morf dlroW olleH
Vowel Count: 9
Spaces Replaced: Hello-World-from-Python-Essentials
```

Checking the vowel count by hand: H**e**ll**o** W**o**rld fr**o**m
P**y**th**o**n **E**ss**e**nt**ia**ls → e, o, o, o, o, E, e, i, a = **9**.
`y` is not counted, which matches the lab's list of a, e, i, o, u.

Note that `Reversed` reverses the whole string character by character, so the
words come out backwards too — that is what "reverse order" asks for.
`Spaces Replaced` changes every space, not just the first.

---

## Task 2 — `list_manager.py`

One session exercising every menu option and every error path: three adds, a
display, a valid removal, a second display, a non-integer number, an
out-of-range index, a non-integer index, an unrecognised menu choice, and quit.

```

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: a
Enter an integer: 10
Added 10

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: a
Enter an integer: 20
Added 20

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: a
Enter an integer: 30
Added 30

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: c
Current list: [10, 20, 30]

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: b
Enter the index to remove: 1
Removed 20 from index 1

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: c
Current list: [10, 30]

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: a
Enter an integer: abc
Error: that is not a whole number.

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: b
Enter the index to remove: 9
Error: there is no item at index 9 - the list has 2 items.

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: b
Enter the index to remove: x
Error: the index must be a whole number.

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: z
Error: please choose a, b, c, or d.

List Manager
(a) Add a number
(b) Remove a number
(c) Display the list
(d) Quit
Choose an option: d
Goodbye.
```

The program never stops on an error. After each error message the menu is
printed again and the list keeps its contents.

---

## Task 3 — `age_validator.py`

Three runs: an accepted age, an age above the allowed range, and text that is
not a number at all.

### Valid age

```
Enter your age: 41
Age accepted: 41
```

### Age outside 0–120

```
Enter your age: 150
Error: Age must be between 0 and 120. You entered 150.
```

This is the `ValueError` raised by `validate_age` itself.

### Input that is not a number

```
Enter your age: forty
Error: invalid literal for int() with base 10: 'forty'
```

This `ValueError` comes from `int()`, not from `validate_age` — the function is
never reached. Both land in the same `except ValueError` block, which is why a
bad entry is reported instead of crashing.

---

## Summary

| Script | Result | Exit status |
| --- | --- | --- |
| `string_manipulation.py` | Uppercase, reversed, vowel count, and hyphenated output all printed with labels | 0 |
| `list_manager.py` | Add, remove, display, and quit all work; non-integer input and invalid index both handled | 0 |
| `age_validator.py` | Accepts a valid age; catches both an out-of-range age and non-numeric input | 0 |
