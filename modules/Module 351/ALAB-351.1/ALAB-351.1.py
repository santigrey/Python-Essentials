# Print the same two lines from Part 2.
print("Hello, World!")
print("Welcome to Python programming.")

# Ask the user for their name. input() shows the question and waits for typing.
name = input("What is your name? ")

# .strip() removes spaces at the start and end, so "   " becomes "".
name = name.strip()

# If the name is empty, use a friendly fallback instead of printing a blank name.
if name == "":
    name = "friend"

# An f-string lets me drop the variable straight into the sentence.
print(f"Hello, {name}! Glad to have you learning Python.")
