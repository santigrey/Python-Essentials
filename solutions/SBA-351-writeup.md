# SBA 351 - Contact Book: Write-Up

## Program structure

The program is one file, `SBA-351.py`, built out of small functions that each do
one job. The helpers at the top all return a value; the feature functions below
them handle the printing and prompting.

### Helper functions

| Function | Returns | What it does |
| --- | --- | --- |
| `is_valid_phone(number)` | `bool` | `True` only for a digits-only string of 7-15 characters. |
| `find_existing_name(contacts, name)` | stored name or `None` | Finds a name already in the book while ignoring capitalization. |
| `find_matches(contacts, term)` | `dict` | The contacts whose name contains `term`, ignoring capitalization. |
| `contact_list_is_empty(contacts)` | `bool` | Prints `The contact list is empty.` and returns `True` when nothing is stored. |
| `print_contact(name, phone)` | - | Prints one contact in the standard `name: number` format. |

### Feature functions

| Function | What it does |
| --- | --- |
| `add_contact(contacts)` | Asks for a name and a number, rejects blanks, duplicates, and bad numbers, then stores the pair. |
| `view_contacts(contacts)` | Prints every contact, or the empty-list message. |
| `search_contact(contacts)` | Asks for text and prints every contact whose name contains it. |
| `delete_contact(contacts)` | Removes a contact by name, or says it does not exist. |
| `show_menu()` | Prints the five menu options. |
| `get_choice()` | Reads the menu number and returns `0` if the answer was not a number. |
| `main()` | The loop that shows the menu and calls the function matching the choice. |

Each of the four feature functions takes the `contacts` dictionary as a
parameter, so no function reaches for a global variable.

## Data flow

`main()` creates one empty dictionary named `contacts` and then loops. Every
time through the loop it prints the menu, reads a choice, and hands that same
dictionary to whichever feature function the user picked.

Because a dictionary is mutable, the feature functions change the caller's
dictionary directly - there is nothing to return and nothing to reassign. The
name is the key and the phone number is the value, which is what makes names
unique automatically and makes a lookup like `name in contacts` instant.

```
main() ──► contacts = {}
             │
             ├─► add_contact(contacts)      adds a key
             │     ├─ find_existing_name() ─► duplicate check
             │     └─ is_valid_phone() ─────► phone check
             │
             ├─► view_contacts(contacts)    reads all keys
             │     └─ contact_list_is_empty(), print_contact()
             │
             ├─► search_contact(contacts)   reads matching keys
             │     └─ find_matches() ───────► dict of matches
             │
             └─► delete_contact(contacts)   removes a key
                   └─ find_existing_name()
```

The loop ends only on choice `5`, which prints a goodbye and `break`s.

## Challenges solved

**Duplicate names.** `contacts[name] = phone` happily overwrites an existing
key without warning, which would quietly destroy a saved number. The fix was to
check for the name first and return early with a message before the assignment
ever runs. Comparing with `name in contacts` alone would still let
`alice johnson` be stored next to `Alice Johnson`, so `find_existing_name()`
compares in lowercase and returns the spelling already on file. `delete_contact()`
uses the same helper, so a contact can be deleted without matching the original
capitalization.

**Crashing on non-numeric menu input.** `int(input(...))` raises a `ValueError`
the moment someone types `abc`. `get_choice()` wraps that call in
`try`/`except ValueError` and returns `0` instead. Since `0` is not one of the
five options, `main()` falls through to its `else` branch, prints the error, and
shows the menu again - no crash and no duplicated error handling.

**Phone validation.** `.isdigit()` alone would accept a single digit or a
fifty-digit string, so `is_valid_phone()` also checks the length against the
`MIN_PHONE_DIGITS` and `MAX_PHONE_DIGITS` constants. Keeping the limits in
named constants means the rule is stated in one place and the error message
stays in step with it.

**Partial and case-insensitive search.** Comparing the names directly would only
find exact matches. `find_matches()` lowercases both the search text and the
name before using the `in` operator, so `al` finds `Alice Johnson`. Returning a
dictionary rather than printing inside the loop keeps the matching logic
separate from the display.

**Repeating the same few lines.** The empty-list check and the `name: number`
print were each needed in more than one place. Pulling them into
`contact_list_is_empty()` and `print_contact()` means the wording lives in one
spot, so it can never drift between the view and search screens.

**Exiting cleanly.** Pressing Ctrl+C, or reaching the end of piped input, would
end the program with a traceback. The call to `main()` is wrapped in
`try`/`except (EOFError, KeyboardInterrupt)` so those end the program with a
goodbye message instead.

## Optional enhancements implemented

- **Alphabetical display.** `view_contacts()` loops over `sorted(contacts)` and
  `find_matches()` builds its results from `sorted(contacts)`, so contacts
  always print in alphabetical order regardless of the order they were added.

Not implemented: multiple phone numbers per contact, and saving/loading to a
file.
