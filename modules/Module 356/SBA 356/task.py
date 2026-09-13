# SBA 356 - Task 1: Task class
# Represents a single to-do item: a title, an optional due date, and a
# completed flag. __str__ formats it for display in the task list.

class Task:
    def __init__(self, title, due_date=None, completed=False):
        self.title = title
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        mark = "X" if self.completed else "-"
        if self.due_date:
            return f"[{mark}] {self.title} (due {self.due_date})"
        return f"[{mark}] {self.title}"
