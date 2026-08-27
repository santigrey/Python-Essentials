# NetAcad Python Essentials 1 - Module 4 Project: Tic-Tac-Toe

**Name:** James Sloan
**Course:** Python Essentials (UCI 3052) - NetAcad PE1, Module 4
**Date:** August 27, 2026

A simplified tic-tac-toe game. The computer plays `X` and always opens in the
middle square; the user plays `O` and picks a square by its number. Free squares
still display their own number, so the board doubles as the menu.

## Files

| File | Purpose |
| --- | --- |
| `tic_tac_toe.py` | The complete game — board setup, the five required functions, and the game loop. |

## How to run

```bash
python3 tic_tac_toe.py
```

Python 3.9 or newer. Uses only `randrange` from the standard-library `random`
module; no third-party packages required.

## Required functions

| Function | What it does |
| --- | --- |
| `display_board(board)` | Prints the board. Each square is three lines tall, with a `+-------+` separator above every row and one more to close the bottom. |
| `enter_move(board)` | Asks for the user's move, rejects anything that is not a whole number from 1 to 9 or points at a taken square, then writes `'O'`. |
| `make_list_of_free_fields(board)` | Returns a list of `(row, column)` tuples for every square that still holds a number. |
| `victory_for(board, sign)` | Returns `True` if that sign holds a full row, column, or diagonal — eight winning lines in total. |
| `draw_move(board)` | Picks one free square at random with `randrange()` and writes `'X'`. |

`make_board()` is a small helper that builds the nested list, filling each square
with its own number.

## How the board is stored

A three-element list whose elements are themselves three-element lists, one per
row, so any square is reached with `board[row][column]`. A free square holds an
integer (its number); a taken square holds `'O'` or `'X'`. That difference is
what `make_list_of_free_fields()` tests to tell free from taken.

Square numbers run row by row, so number `n` sits at
`row = (n - 1) // 3`, `column = (n - 1) % 3`.

---

## Example output

Opening board, after the computer's first move:

```
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
Enter your move:
```

Rejected input — text, out of range, and an occupied square:

```
Enter your move: abc
Please enter a number.
Enter your move: 99
Pick a number from 1 to 9.
Enter your move: 5
That square is already taken.
Enter your move: 1
```

After the accepted move:

```
+-------+-------+-------+
|       |       |       |
|   O   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
```

The game ends with one of three messages: `You won!`, `I won!`, or `It's a tie.`
