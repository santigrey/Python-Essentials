# SBA 351 - Contact Book: Rubric Check

Each rubric line mapped to where it is satisfied in `SBA-351.py`, with the
evidence in `SBA-351-interaction-log.md`. Line numbers refer to the committed
version of the script.

## Functionality - 55 pts

| Criterion | Pts | Where it is met | Log evidence |
| --- | --- | --- | --- |
| Add Contact works | 9 | `add_contact()` stores `contacts[name] = phone`; duplicates caught by `find_existing_name()` before the assignment, blank names rejected. | Session 1: two adds, exact duplicate rejected, `alice johnson` case-variant duplicate rejected, blank name rejected. |
| View Contacts works | 9 | `view_contacts()` prints every pair; `contact_list_is_empty()` prints `The contact list is empty.` | Session 1: two views. Session 2: empty-list message. |
| Search Contact works | 9 | `search_contact()` with `find_matches()`; exact and partial, case-insensitive; reports when nothing matches. | Session 1: `al` finds `Alice Johnson`; `Zach` reports no match. |
| Delete Contact works | 9 | `delete_contact()` uses `del contacts[existing_name]`, or reports the name does not exist. | Session 1: `bob smith` deletes `Bob Smith`. Session 2: deleting a missing name reported. |
| Menu Loop and Exit | 9 | `while True` in `main()` re-shows the menu after every action; choice `5` prints `Goodbye!` and `break`s. Ctrl+C / end-of-input caught at the bottom of the file. | Both sessions: menu repeats after every action, clean exit on `5`. |
| Data Handling | 10 | Contacts stored in a dictionary keyed by name, so names are unique by construction; duplicate check is case-insensitive so one person cannot be stored twice; the same dictionary object is passed to every feature function. | Session 1: duplicate attempts leave the stored number untouched. |

## Code Design - 18 pts

| Criterion | Pts | Where it is met |
| --- | --- | --- |
| Uses functions to organize code | 9 | Twelve functions. Each menu feature has its own function taking `contacts`: `add_contact`, `view_contacts`, `search_contact`, `delete_contact`. Menu handling is split into `show_menu`, `get_choice`, and `main`. |
| Code reusability and modularity | 9 | Shared logic is factored into helpers rather than repeated: `find_existing_name()` is used by both add and delete, `contact_list_is_empty()` by both view and search, `print_contact()` by both display paths, `is_valid_phone()` isolates the phone rule, `find_matches()` isolates the search rule. The phone limits live in the `MIN_PHONE_DIGITS` / `MAX_PHONE_DIGITS` constants so the rule and its error message cannot drift apart. |

## User Input Handling and Validation - 9 pts

| Criterion | Pts | Where it is met | Log evidence |
| --- | --- | --- | --- |
| Menu input validation | 4 | `get_choice()` wraps `int(input(...))` in `try`/`except ValueError` and returns `0`; `main()`'s `else` branch catches `0` and anything outside 1-5. | Session 1: `abc` and `9` both print the error and re-show the menu. |
| Input validation for adding contacts | 5 | `add_contact()` rejects a blank name after `.strip()`, rejects a duplicate name, and rejects a phone number failing `is_valid_phone()` (digits only, 7-15 digits). | Session 1: blank name rejected, `555-1234` rejected with the reason. |

## Use of Concepts - 9 pts

| Criterion | Pts | Where it is met |
| --- | --- | --- |
| Conditionals | 2 | `if`/`elif`/`else` chain in `main()` for the menu; `if` guards for blank name, duplicate name, invalid phone, empty term, and no matches. |
| Loops | 2 | `while True` menu loop in `main()`; `for` loops in `view_contacts()`, `find_matches()`, `find_existing_name()`, and the match display. |
| Data structures | 2 | A dictionary for the contact book (name to number), and `find_matches()` builds and returns a second dictionary of results. |
| try/except for error handling | 1 | `try`/`except ValueError` in `get_choice()`; `try`/`except (EOFError, KeyboardInterrupt)` around the call to `main()`. |
| Functions and return values | 2 | `is_valid_phone()` returns a bool, `contact_list_is_empty()` returns a bool, `get_choice()` returns an int, `find_existing_name()` returns a name or `None`, `find_matches()` returns a dictionary. Callers branch on those return values. |

## Code Quality and Documentation - 9 pts

| Criterion | Pts | Where it is met |
| --- | --- | --- |
| Code is well-formatted | 4 | Consistent four-space indentation, two blank lines between top-level functions, `snake_case` functions, `UPPER_CASE` constants, section banner comments separating helpers, features, and menu. |
| Comments are present | 4 | A docstring on every function, an assignment header at the top of the file, and inline comments on the tricky parts: why the duplicate check has to come before the assignment, why `get_choice()` returns `0`, why an empty dictionary is falsy, and why Ctrl+C is caught. |
| Meaningful names | 1 | `contacts`, `existing_name`, `matches`, `term`, `is_valid_phone`, `find_existing_name`, `contact_list_is_empty`, `MIN_PHONE_DIGITS`. |

## Not implemented

The optional extra-credit items are not part of the rubric above. Multiple
numbers per contact and file save/load are left out; alphabetical display is
implemented and marked in the code.
