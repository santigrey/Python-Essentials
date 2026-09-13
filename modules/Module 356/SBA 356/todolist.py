# SBA 356 - Task 2 & 4: To-do manager functions
# Operates on a list of Task objects: add, complete, delete, and list (with
# overdue detection), plus save/load for persisting tasks to a CSV file.

import csv
import os
from datetime import date, datetime

from task import Task

TASKS_FILE = "tasks.csv"


def add_task(task_list, title, due_date=None):
    parsed_date = None
    if due_date:
        try:
            parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
        except ValueError:
            print(f"Error: '{due_date}' is not a valid date (expected YYYY-MM-DD). Task added with no due date.")
    task_list.append(Task(title, parsed_date))
    print(f"Added: {title}")


def complete_task(task_list, index):
    try:
        task_list[index].completed = True
        print(f"Marked complete: {task_list[index].title}")
    except IndexError:
        print(f"Error: no task at index {index}.")


def delete_task(task_list, index):
    try:
        removed = task_list.pop(index)
        print(f"Deleted: {removed.title}")
    except IndexError:
        print(f"Error: no task at index {index}.")


def list_tasks(task_list):
    if not task_list:
        print("No tasks yet.")
        return
    today = date.today()
    for i, task in enumerate(task_list):
        overdue = "  [OVERDUE]" if task.due_date and not task.completed and task.due_date < today else ""
        print(f"{i}: {task}{overdue}")


def load_tasks():
    task_list = []
    if not os.path.exists(TASKS_FILE):
        print(f"{TASKS_FILE} not found - starting with an empty list.")
        return task_list
    try:
        with open(TASKS_FILE, "r", newline="") as f:
            reader = csv.reader(f)
            for title, due_date, completed in reader:
                due = date.fromisoformat(due_date) if due_date else None
                task_list.append(Task(title, due, completed == "True"))
        print(f"Loaded {len(task_list)} task(s) from {TASKS_FILE}.")
    except (OSError, ValueError) as e:
        print(f"Error loading {TASKS_FILE}: {e}. Starting with an empty list.")
    return task_list


def save_tasks(task_list):
    try:
        with open(TASKS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            for task in task_list:
                writer.writerow([task.title, task.due_date or "", task.completed])
        print(f"Saved {len(task_list)} task(s) to {TASKS_FILE}.")
    except OSError as e:
        print(f"Error saving {TASKS_FILE}: {e}")
