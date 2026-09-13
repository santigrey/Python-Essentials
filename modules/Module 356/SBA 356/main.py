# SBA 356 - Task 3: Text menu interface
# Loads any saved tasks on startup, then loops a menu that adds, completes,
# deletes, and lists tasks, saving back to disk on request before quitting.

from todolist import add_task, complete_task, delete_task, list_tasks, load_tasks, save_tasks

tasks = load_tasks()

while True:
    print()
    print("To-Do List Manager")
    print("(A) Add a task")
    print("(C) Mark a task completed")
    print("(D) Delete a task")
    print("(L) List tasks")
    print("(Q) Quit")

    choice = input("Choose an option: ").strip().upper()

    if choice == "A":
        title = input("Task title: ")
        due_date = input("Due date (YYYY-MM-DD, blank for none): ").strip()
        add_task(tasks, title, due_date or None)

    elif choice == "C":
        list_tasks(tasks)
        try:
            index = int(input("Index to mark complete: "))
            complete_task(tasks, index)
        except ValueError:
            print("Error: index must be a whole number.")

    elif choice == "D":
        list_tasks(tasks)
        try:
            index = int(input("Index to delete: "))
            delete_task(tasks, index)
        except ValueError:
            print("Error: index must be a whole number.")

    elif choice == "L":
        list_tasks(tasks)

    elif choice == "Q":
        save_choice = input("Save before quitting? (y/n): ").strip().lower()
        if save_choice == "y":
            save_tasks(tasks)
        print("Goodbye.")
        break

    else:
        print("Error: please choose A, C, D, L, or Q.")
