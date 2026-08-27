# ALAB 351.4 - Part 2: Data Processing
# James Sloan
#
# Averages the grades stored in a dictionary of courses. One course has no
# grades at all, which is the edge case the exception handling is there for.


# ---------------------------------------------------------------------------
# get_average_grade() averages a tuple of numbers.
#
# Parameter: grades_tuple, a tuple of numeric grades.
# Returns: the average, or None if the tuple is empty.
#
# sum() adds the grades and len() counts them. If the tuple is empty len() is
# 0, and dividing by 0 raises ZeroDivisionError. Catching it and returning
# None means the caller gets an answer it can check rather than a crash.
# ---------------------------------------------------------------------------
def get_average_grade(grades_tuple):
    try:
        return sum(grades_tuple) / len(grades_tuple)
    except ZeroDivisionError:
        print("  Warning: no grades to average.")
        return None


# ---------------------------------------------------------------------------
# The keys are course names and the values are tuples of grades.
# Art is deliberately empty to trigger the edge case above.
# ---------------------------------------------------------------------------
course_grades = {
    "Math": (88, 92, 79, 85, 90),
    "Science": (75, 80, 68, 91),
    "History": (95, 89, 100),
    "Art": (),
}

print("Course Averages")
print("===============")

for course, grades in course_grades.items():
    average = get_average_grade(grades)

    # get_average_grade() returns None for the empty course, so check for that
    # before trying to format the number.
    if average is None:
        print(f"The average grade for {course} could not be calculated.")
    else:
        # :.1f rounds to one decimal place for display.
        print(f"The average grade for {course} is {average:.1f}")
