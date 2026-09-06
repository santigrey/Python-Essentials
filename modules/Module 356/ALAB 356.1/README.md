# ALAB 356.1 - Modules, Packages, and PIP

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** September 6, 2026

Four Python scripts covering built-in modules, a custom module organized as a
package, and a third-party package installed with PIP.

## Files

| File | Purpose |
| --- | --- |
| `builtin_usage.py` | Task 1 — imports `math`, `random`, and `platform`; generates a random integer from 1 to 100, floors its square root, and prints the OS name and Python version with descriptive labels. |
| `mypackage/__init__.py` | Task 2 — empty file that marks `mypackage` as a package. |
| `mypackage/utilities.py` | Task 2 — the custom module; defines `greet(name)` and `factorial(n)`. |
| `use_utilities.py` | Task 2 — imports the module with `from mypackage import utilities` and prints the result of both functions. |
| `external_package.py` | Task 3 — uses the third-party `colorama` package to print colored text. |

## How to run

```bash
cd "modules/Module 356/ALAB 356.1"
python3 builtin_usage.py
python3 use_utilities.py
python3 external_package.py
```

`use_utilities.py` finds `mypackage` because Python adds the folder the script
itself lives in to the import path, so the import works no matter which folder
you run it from. What breaks it is moving `use_utilities.py` out of this folder
and away from `mypackage`.

Python 3.9 or newer. `builtin_usage.py` and `use_utilities.py` need no
third-party packages. `external_package.py` needs `colorama`:

```bash
pip install colorama
```

Installed for this lab with `pip3 install --user colorama`, which reported
`Successfully installed colorama-0.4.6`.

---

## Example output

### builtin_usage.py

The random number changes every run, so the floored square root changes with it.
Two runs:

```
Random Number: 81
Square Root (floored): 9
Operating System: Darwin
Python Version: 3.13.2
```

```
Random Number: 37
Square Root (floored): 6
Operating System: Darwin
Python Version: 3.13.2
```

`platform.system()` reports `Darwin` on a Mac, not `macOS` — Darwin is the name
of the underlying operating system. On Windows it prints `Windows`, on Linux
`Linux`.

### use_utilities.py

```
greet():
Hello, James! Welcome to Python modules.

factorial():
5! = 120
7! = 5040
```

### external_package.py

Each line prints in the color named at the start of it. Colors do not survive
being copied into a text file, so this is what the terminal shows:

```
Green text: colorama is installed and working.      <- printed in green
Red text: this line is a warning.                   <- printed in red
Cyan text: this line is a note.                     <- printed in cyan
Bright yellow text: this line stands out.           <- printed in bright yellow
Back to the normal terminal color.                  <- printed in the default color
```

---

## Rubric mapping

Rubric taken from the lab text at
`ps-lms.vercel.app/curriculum/netacad/pe2/lab-1/`, which is the page the Canvas
assignment embeds.

| Criterion | Points | Where it is met |
| --- | --- | --- |
| Built-in Modules | 10 | `builtin_usage.py` — all three modules imported and used; four labeled outputs |
| Custom Module Creation | 15 | `mypackage/utilities.py` defines `greet` and `factorial`; `use_utilities.py` imports and calls both |
| Package Organization | 5 | `mypackage/` folder with an empty `__init__.py`, imported as `from mypackage import utilities` |
| PIP Package Integration | 10 | `colorama` installed with PIP; `external_package.py` demonstrates it and documents the install in its first line |
| Code Quality | 5 | Comments on every script, descriptive print labels, this README with example outputs |
