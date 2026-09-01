# SBA 351 - Contact Book: Write-Up

## Program structure

The program is one file, `SBA-351.py`, built out of small functions that each do
one job.

| Function | What it does |
| --- | --- |
| `is_valid_phone(number)` | Helper. Returns `True` only for a digits-only string of 7-15 characters. |
| `add_contact(contacts)` | Asks for a name and a number, rejects blanks, duplicates, and bad numbers, then stores the pair. |
| `view_contacts(contacts)` | Prints every contact, or `The contact list is empty.` |
| `search_contact(contacts)` | Asks for text and prints every contact whose name contains it. |
| `delete_contact(contacts)` | Removes a contact by exact name, or says it does not exist. |
| `show_menu()` | Prints the five menu options. |
| `get_choice()` | Reads the menu number and returns `0` if the answer was not a number. |
| `main()` | The loop that shows the menu and calls the function matching the choice. |

Each of the four feature functions takes the `contacts` dictionary as a
parameter, so no function reaches for a global variable.

## Data flow

`main()` creates one empty dictionary named `contacts` and then loops. Every
time through the loop it prints the menu, reads a choice, and hands that same
dictionary to whichever feature function the user picked.

Because a dictionary is mutable, the functions change the caller's dictionary
directly - there is nothing to return and nothing to reassign. The name is the
key and the phone number is the value, which is what makes names unique
automatically and makes a lookup like `name in contacts` instant.

```
main() ──► contacts = {}
             │
             ├─► add_contact(contacts)      adds a key
             ├─► view_contacts(contacts)    reads all keys
             ├─► search_contact(contacts)   reads matching keys
             └─► delete_contact(contacts)   removes a key
```

The loop ends only on choice `5`, which prints a goodbye and `break`s.

## Challenges solved

**Duplicate names.** `contacts[name] = phone` happily overwrites an existing
key without warning, which would quietly destroy a saved number. The fix was to
check `if name in contacts:` and return early with a message before the
assignment ever runs.

**Crashing on non-numeric menu input.** `int(input(...))` raises a `ValueError`
the moment someone types `abc`. `get_choice()` wraps that call in
`try`/`except ValueError` and returns `0` instead. Since `0` is not one of the
five options, `main()` falls through to its `else` branch, prints the error, and
shows the menu again - no crash and no duplicated error handling.

**Phone validation.** `.isdigit()` alone would accept a single digit or a
fifty-digit string, so `is_valid_phone()` also checks the length against the
`MIN_PHONE_DIGITS` and `MAX_PHONE_DIGITS` constants. Keeping the limits in
named constants means the rule is stated in one place.

**Partial and case-insensitive search.** Comparing the names directly would only
find exact matches. Lowercasing both the search text and the name before using
the `in` operator makes `al` find `Alice Johnson`.

**Exiting cleanly.** Pressing Ctrl+C, or reaching the end of piped input, would
end the program with a traceback. The call to `main()` is wrapped in
`try`/`except (EOFError, KeyboardInterrupt)` so those end the program with a
goodbye message instead.

## Optional enhancements implemented

- **Alphabetical display.** `view_contacts()` and `search_contact()` loop over
  `sorted(contacts)`, so contacts always print in alphabetical order regardless
  of the order they were added.

Not implemented: multiple phone numbers per contact, and saving/loading to a
file.
