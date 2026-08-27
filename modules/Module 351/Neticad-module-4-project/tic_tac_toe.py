# NetAcad Python Essentials 1 - Module 4 Project: Tic-Tac-Toe
# James Sloan
#
# The computer plays 'X' and always opens in the middle. The user plays 'O'
# and chooses a square by its number. Free squares still show their number.

from random import randrange


# ---------------------------------------------------------------------------
# The board is a three-element list, and each of those elements is another
# three-element list standing for one row. That is what lets any square be
# reached with board[row][column].
#
# A free square holds its own number (1 through 9, counted row by row), so the
# same value is both the label on screen and the thing the user types.
# ---------------------------------------------------------------------------
def make_board():
    board = []
    for row in range(3):
        board.append([])
        for col in range(3):
            # Row 0 holds 1-3, row 1 holds 4-6, row 2 holds 7-9.
            board[row].append(3 * row + col + 1)
    return board


# ---------------------------------------------------------------------------
# display_board() accepts the board's current status and prints it out.
#
# Every square is three text lines tall: a blank line, the line carrying the
# symbol, then another blank line. The "+-------+" separator is printed above
# each row and once more at the very bottom to close the last row off.
# ---------------------------------------------------------------------------
def display_board(board):
    separator = "+-------+-------+-------+"
    blank = "|       |       |       |"

    for row in range(3):
        print(separator)
        print(blank)
        # Build the middle line one square at a time so each entry sits in the
        # same amount of space.
        middle = "|"
        for col in range(3):
            middle = middle + "   " + str(board[row][col]) + "   |"
        print(middle)
        print(blank)
    print(separator)


# ---------------------------------------------------------------------------
# make_list_of_free_fields() browses the board and builds a list of the free
# squares. Each entry is a tuple holding that square's row and column.
#
# A square is free when it still holds a number. Anything holding 'O' or 'X'
# has been taken, so checking the type is enough to tell them apart.
# ---------------------------------------------------------------------------
def make_list_of_free_fields(board):
    free = []
    for row in range(3):
        for col in range(3):
            if isinstance(board[row][col], int):
                free.append((row, col))
    return free


# ---------------------------------------------------------------------------
# victory_for() checks whether the player using the given sign has won.
#
# There are eight ways to win: three rows, three columns, and two diagonals.
# The function returns True the moment it finds one and False if none match.
# ---------------------------------------------------------------------------
def victory_for(board, sign):
    for i in range(3):
        # A full row: all three columns of row i.
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return True
        # A full column: all three rows of column i.
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True

    # Top-left to bottom-right.
    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True
    # Top-right to bottom-left.
    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


# ---------------------------------------------------------------------------
# enter_move() asks the user for a move, checks it, and updates the board.
#
# The move is only accepted when it is a whole number from 1 to 9 that points
# at a square nobody has taken yet. Anything else sends the loop round again.
# int() raises ValueError on text that is not a number, so try/except keeps a
# typo from crashing the game.
# ---------------------------------------------------------------------------
def enter_move(board):
    free = make_list_of_free_fields(board)

    while True:
        try:
            move = int(input("Enter your move: "))
        except ValueError:
            print("Please enter a number.")
            continue

        if move < 1 or move > 9:
            print("Pick a number from 1 to 9.")
            continue

        # Turn the square number back into a row and a column. Subtracting 1
        # first makes the numbering start at 0, which is how lists count.
        row = (move - 1) // 3
        col = (move - 1) % 3

        if (row, col) not in free:
            print("That square is already taken.")
            continue

        board[row][col] = 'O'
        return


# ---------------------------------------------------------------------------
# draw_move() picks one of the free squares at random and puts an 'X' there.
#
# randrange(len(free)) gives a position inside the list of free squares, and
# that entry is the (row, column) pair to fill in.
# ---------------------------------------------------------------------------
def draw_move(board):
    free = make_list_of_free_fields(board)
    if len(free) == 0:
        return

    row, col = free[randrange(len(free))]
    board[row][col] = 'X'


# ---------------------------------------------------------------------------
# The game itself.
# ---------------------------------------------------------------------------
board = make_board()

# The computer always opens in the middle square.
board[1][1] = 'X'
display_board(board)

while True:
    enter_move(board)
    display_board(board)

    if victory_for(board, 'O'):
        print("You won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie.")
        break

    draw_move(board)
    display_board(board)

    if victory_for(board, 'X'):
        print("I won!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("It's a tie.")
        break
