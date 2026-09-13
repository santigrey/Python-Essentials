# ALAB 356.4 - Task 3: Diary Entry Program
# Checks whether diary.txt exists (creating it if not), prompts for entries
# until a blank line, appends each one with a timestamp, then displays the
# whole file.

import os
from datetime import datetime

DIARY_FILE = "diary.txt"

try:
    if not os.path.exists(DIARY_FILE):
        open(DIARY_FILE, "w").close()
        print(f"{DIARY_FILE} did not exist - created it.")
    else:
        print(f"{DIARY_FILE} already exists.")

    while True:
        entry = input("Enter a diary entry (blank to stop): ")
        if entry == "":
            break
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DIARY_FILE, "a") as f:
            f.write(f"[{timestamp}] {entry}\n")

    print()
    print("--- diary.txt contents ---")
    with open(DIARY_FILE, "r") as f:
        print(f.read(), end="")

except OSError as e:
    print("Error accessing the diary file:", e)
