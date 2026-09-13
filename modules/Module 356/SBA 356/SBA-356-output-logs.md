# SBA 356 — Output Logs

Full terminal transcripts. Two runs: the first builds up a task list and
exercises every menu option and error path, saving at the end; the second
is a fresh process that reloads from the saved file to prove persistence.

## Run 1 — build, edit, and save

```
$ python3 main.py
tasks.csv not found - starting with an empty list.

To-Do List Manager
(A) Add a task
(C) Mark a task completed
(D) Delete a task
(L) List tasks
(Q) Quit
Choose an option: A
Task title: Submit assignment
Due date (YYYY-MM-DD, blank for none): 2026-09-15
Added: Submit assignment

To-Do List Manager
...
Choose an option: A
Task title: Buy groceries
Due date (YYYY-MM-DD, blank for none): 2026-01-01
Added: Buy groceries

To-Do List Manager
...
Choose an option: A
Task title: Read a book
Due date (YYYY-MM-DD, blank for none):
Added: Read a book

To-Do List Manager
...
Choose an option: A
Task title: Bad date test
Due date (YYYY-MM-DD, blank for none): not-a-date
Error: 'not-a-date' is not a valid date (expected YYYY-MM-DD). Task added with no due date.
Added: Bad date test

To-Do List Manager
...
Choose an option: L
0: [-] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Read a book
3: [-] Bad date test

To-Do List Manager
...
Choose an option: C
0: [-] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Read a book
3: [-] Bad date test
Index to mark complete: 0
Marked complete: Submit assignment

To-Do List Manager
...
Choose an option: D
0: [X] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Read a book
3: [-] Bad date test
Index to delete: 2
Deleted: Read a book

To-Do List Manager
...
Choose an option: L
0: [X] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Bad date test

To-Do List Manager
...
Choose an option: C
0: [X] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Bad date test
Index to mark complete: 99
Error: no task at index 99.

To-Do List Manager
...
Choose an option: D
0: [X] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Bad date test
Index to delete: abc
Error: index must be a whole number.

To-Do List Manager
...
Choose an option: Z
Error: please choose A, C, D, L, or Q.

To-Do List Manager
...
Choose an option: Q
Save before quitting? (y/n): y
Saved 3 task(s) to tasks.csv.
Goodbye.
```

`tasks.csv` after this run:

```
Submit assignment,2026-09-15,True
Buy groceries,2026-01-01,False
Bad date test,,False
```

## Run 2 — fresh process, reload from disk

```
$ python3 main.py
Loaded 3 task(s) from tasks.csv.

To-Do List Manager
(A) Add a task
(C) Mark a task completed
(D) Delete a task
(L) List tasks
(Q) Quit
Choose an option: L
0: [X] Submit assignment (due 2026-09-15)
1: [-] Buy groceries (due 2026-01-01)  [OVERDUE]
2: [-] Bad date test

To-Do List Manager
...
Choose an option: Q
Save before quitting? (y/n): n
Goodbye.
```

The completed flag on task 0 and the overdue flag on task 1 both survive
the round trip through `tasks.csv` — proof that `load_tasks()` reconstructs
real `Task` objects (with a real `date`, not a string) rather than just
replaying text.

## Additional error paths (not screenshotted, verified separately)

**Loading a corrupted file** — `load_tasks()`'s `except (OSError, ValueError)`
catches a malformed row cleanly instead of crashing:

```
$ python3 main.py
Error loading tasks.csv: too many values to unpack (expected 3, got 7). Starting with an empty list.
```

**Starting with no file at all** — already shown at the top of Run 1:
`tasks.csv not found - starting with an empty list.`
