# ALAB 356.1 — Output Logs

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052)
**Date:** September 6, 2026

Text logs demonstrating that each script works as intended, satisfying the
submission requirement: *"Include example outputs (screenshots or text logs)
demonstrating that each script works as intended."*

Every block below is captured output, copied straight from the run — nothing is
typed by hand. Each command was run from inside the `ALAB 356.1` folder.

**Environment:** macOS (`Darwin`), Python 3.13.2, colorama 0.4.6.

---

## Task 1 — `builtin_usage.py`

Run three times to show the random number changing and the floored square root
changing with it. Exit status 0 each time.

```
$ python3 builtin_usage.py
Random Number: 81
Square Root (floored): 9
Operating System: Darwin
Python Version: 3.13.2
```

```
$ python3 builtin_usage.py
Random Number: 73
Square Root (floored): 8
Operating System: Darwin
Python Version: 3.13.2
```

```
$ python3 builtin_usage.py
Random Number: 55
Square Root (floored): 7
Operating System: Darwin
Python Version: 3.13.2
```

Checking the three by hand: √81 = 9 exactly. √73 ≈ 8.544, floored to 8.
√55 ≈ 7.416, floored to 7. All four labels print as required.

`Darwin` is the operating system name macOS is built on — that is what
`platform.system()` reports on a Mac. It prints `Windows` on Windows and `Linux`
on Linux.

---

## Task 2 — `use_utilities.py`

Imports the custom module out of the package and calls both functions.

```
$ python3 use_utilities.py
greet():
Hello, James! Welcome to Python modules.

factorial():
5! = 120
7! = 5040
```

Checking: 5! = 5 × 4 × 3 × 2 × 1 = 120. 7! = 5040. Both correct.

### Proof the package import resolves

Confirming `mypackage` is a real package and not just a folder that happens to
work:

```
$ python3 -c "import mypackage, mypackage.utilities as u; print(mypackage.__file__); print(u.greet('Kelly')); print(u.factorial(5))"
/Users/jes/.../modules/Module 356/ALAB 356.1/mypackage/__init__.py
Hello, Kelly! Welcome to Python modules.
120
```

`mypackage.__file__` pointing at the real `__init__.py` is what shows this is a
regular package. A folder without `__init__.py` would still import in modern
Python, but as a namespace package, and `__file__` would be `None`.

---

## Task 3 — `external_package.py`

### Installing the package with PIP

First-time install, run on September 6, 2026:

```
$ pip3 install --user colorama
Collecting colorama
  Downloading colorama-0.4.6-py2.py3-none-any.whl.metadata (17 kB)
Downloading colorama-0.4.6-py2.py3-none-any.whl (25 kB)
Installing collected packages: colorama
Successfully installed colorama-0.4.6
```

Running the same command again confirms it is installed:

```
$ pip3 install --user colorama
Requirement already satisfied: colorama in /Users/jes/Library/Python/3.13/lib/python/site-packages (0.4.6)
```

```
$ pip3 show colorama
Name: colorama
Version: 0.4.6
Summary: Cross-platform colored terminal text.
Home-page: https://github.com/tartley/colorama
Author-email: Jonathan Hartley <tartley@tartley.com>
Location: /Users/jes/Library/Python/3.13/lib/python/site-packages
```

### Running the script

```
$ python3 external_package.py
Green text: colorama is installed and working.
Red text: this line is a warning.
Cyan text: this line is a note.
Bright yellow text: this line stands out.
Back to the normal terminal color.
```

In a terminal each of those first four lines appears in the color it names. A
text log cannot carry color, so the next section shows the actual codes as proof.

### Proof the colors are real

colorama produces color by emitting ANSI escape codes. It strips them when output
is redirected to a file, which is why the block above is plain. Running the script
through a pseudo-terminal instead makes colorama treat it as a real terminal, and
the codes appear. `ESC` below stands for the invisible escape character:

```
ESC[32mGreen text: colorama is installed and working.ESC[0m
ESC[0mESC[31mRed text: this line is a warning.ESC[0m
ESC[0mESC[36mCyan text: this line is a note.ESC[0m
ESC[0mESC[1mESC[33mBright yellow text: this line stands out.ESC[0m
ESC[0mBack to the normal terminal color.ESC[0m
```

Reading the codes: `32` is green, `31` red, `36` cyan, `1` bright and `33` yellow,
and `0` resets to the default. The trailing `ESC[0m` on every line is
`init(autoreset=True)` doing its job — it puts the color back to normal after each
`print`, so the color never leaks into the next line or into the shell prompt after
the script exits.

---

## Screenshots

The same three scripts captured running in Terminal, saved alongside this file:

| File | Shows |
| --- | --- |
| `screenshot-1-builtin_usage.png` | Three consecutive runs — 51 → 7, 48 → 6, 73 → 8 — with the command line visible each time |
| `screenshot-2-use_utilities.png` | `greet()` and `factorial()` called through the package import |
| `screenshot-3-external_package.png` | colorama printing in actual green, red, cyan, and bright yellow |

Checking the first screenshot by hand: √51 ≈ 7.14 floored to 7, √48 ≈ 6.93 floored
to 6, √73 ≈ 8.54 floored to 8. All three correct.

One thing to note in the colorama screenshot: the last line, "Back to the normal
terminal color," also appears green. That is not colorama still colouring it — it
is this Terminal profile's own default text colour, which happens to be green.
That line is the proof `init(autoreset=True)` worked: the colour returned to the
terminal default instead of staying yellow.

---

## Summary

| Script | Result | Exit status |
| --- | --- | --- |
| `builtin_usage.py` | Random number, floored square root, OS name, and Python version all print with labels | 0 |
| `use_utilities.py` | `greet()` and `factorial()` both imported from `mypackage` and called successfully | 0 |
| `external_package.py` | colorama installed with PIP and printing colored text | 0 |
