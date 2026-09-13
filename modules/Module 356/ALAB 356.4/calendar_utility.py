# ALAB 356.4 - Task 4: Date and Calendar Utility
# Prompts for a year and month, prints that month's calendar grid, and
# reports whether today's date falls within it.

import calendar
from datetime import date

try:
    year = int(input("Enter a year: "))
    month = int(input("Enter a month (1-12): "))
    if not 1 <= month <= 12:
        raise ValueError(f"month must be between 1 and 12, got {month}")

    print()
    print(calendar.month(year, month))

    today = date.today()
    if today.year == year and today.month == month:
        print(f"Today ({today}) is within {calendar.month_name[month]} {year}.")
    else:
        print(f"Today ({today}) is NOT within {calendar.month_name[month]} {year}.")

except ValueError as e:
    print("Error:", e)
