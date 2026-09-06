# ALAB 356.2 - Task 2: List Management with Error Handling
# A menu-driven program that adds to, removes from, and displays a list of
# integers. try/except keeps a bad entry from ending the program.

numbers = []

while True:
    print()
    print("List Manager")
    print("(a) Add a number")
    print("(b) Remove a number")
    print("(c) Display the list")
    print("(d) Quit")

    choice = input("Choose an option: ").lower()

    if choice == "a":
        # int() raises a ValueError if the text is not a whole number.
        try:
            number = int(input("Enter an integer: "))
            numbers.append(number)
            print("Added", number)
        except ValueError:
            print("Error: that is not a whole number.")

    elif choice == "b":
        # Two things can go wrong here, so both are caught separately:
        # a non-numeric index (ValueError) and an out-of-range one (IndexError).
        try:
            index = int(input("Enter the index to remove: "))
            removed = numbers.pop(index)
            print("Removed", removed, "from index", index)
        except ValueError:
            print("Error: the index must be a whole number.")
        except IndexError:
            print("Error: there is no item at index", index, "- the list has", len(numbers), "items.")

    elif choice == "c":
        print("Current list:", numbers)

    elif choice == "d":
        print("Goodbye.")
        break

    else:
        print("Error: please choose a, b, c, or d.")
