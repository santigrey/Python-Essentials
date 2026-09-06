# ALAB 356.2 - Strings, String and List Methods, Exceptions

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** September 6, 2026

Three Python scripts covering string methods, a menu-driven list manager with
error handling, and a custom exception raised by an age validator.

## Files

| File | Purpose |
| --- | --- |
| `string_manipulation.py` | Task 1 — asks for a sentence, then prints it uppercased, reversed, its vowel count, and with every space replaced by a hyphen. |
| `list_manager.py` | Task 2 — menu-driven list of integers with add, remove, display, and quit, wrapped in `try`/`except` so a bad entry never stops the program. |
| `age_validator.py` | Task 3 — `validate_age()` raises a `ValueError` outside 0–120; the script catches it and reports the message. |
| `ALAB-356.2-Canvas-Submission.pdf` | The one-page PDF submitted to Canvas — direct clickable links to each script. |
| `ALAB-356.2-output-logs.md` | Captured terminal transcripts for all three scripts, including every error path. |
| `screenshot-1-string_manipulation.png`<br>`screenshot-2a-list_manager-operations.png`<br>`screenshot-2b-list_manager-errors.png`<br>`screenshot-3-age_validator.png` | Terminal screenshots of each script running. |

## How to run

```bash
cd "modules/Module 356/ALAB-356.2"
python3 string_manipulation.py
python3 list_manager.py
python3 age_validator.py
```

Python 3.9 or newer. No third-party packages. All three scripts ask for input.

---

## Example output

### string_manipulation.py

```
Enter a sentence: Hello World from Python Essentials
Uppercase: HELLO WORLD FROM PYTHON ESSENTIALS
Reversed: slaitnessE nohtyP morf dlroW olleH
Vowel Count: 9
Spaces Replaced: Hello-World-from-Python-Essentials
```

`Reversed` reverses the whole string character by character, so the words come
out backwards as well. The vowel count is 9 — `y` is not counted, matching the
lab's list of a, e, i, o, u.

### list_manager.py

Adding two numbers, removing index 0, displaying, then quitting:

```
Choose an option: a
Enter an integer: 10
Added 10
Choose an option: a
Enter an integer: 20
Added 20
Choose an option: b
Enter the index to remove: 0
Removed 10 from index 0
Choose an option: c
Current list: [20]
Choose an option: d
Goodbye.
```

The three error paths, none of which stop the program:

```
Choose an option: a
Enter an integer: abc
Error: that is not a whole number.

Choose an option: b
Enter the index to remove: 9
Error: there is no item at index 9 - the list has 0 items.

Choose an option: b
Enter the index to remove: x
Error: the index must be a whole number.
```

### age_validator.py

```
Enter your age: 41
Age accepted: 41
```

```
Enter your age: 150
Error: Age must be between 0 and 120. You entered 150.
```

```
Enter your age: forty
Error: invalid literal for int() with base 10: 'forty'
```

The second error comes from `validate_age` itself. The third comes from `int()`
before the function is ever called — both are `ValueError`, so one `except`
block covers them.

Full transcripts are in `ALAB-356.2-output-logs.md`.

---

## Rubric mapping

Rubric taken from the lab text at
`ps-lms.vercel.app/curriculum/netacad/pe2/lab-2/`, which is the page the Canvas
assignment embeds.

| Criterion | Points | Where it is met |
| --- | --- | --- |
| String Operations | 15 | `string_manipulation.py` — all four operations, each printed with a clear label |
| List Management Functionality | 15 | `list_manager.py` — add, remove via `pop(index)`, display, and quit, in a loop |
| Exception Handling in List Management | 10 | `try`/`except ValueError` on both the number and the index, plus `except IndexError` on removal |
| Custom Exception Usage (Age Validator) | 5 | `validate_age()` raises `ValueError` outside 0–120; the caller catches and prints it |
| Code Organization and Style | 5 | Comments in every script, descriptive names, labeled output, this README and the logs |
