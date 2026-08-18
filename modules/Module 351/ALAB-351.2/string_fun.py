# ALAB 351.2 - Bonus: String Fun
# James Sloan
#
# Asks for a single word and reports a few facts about it.

print("String Fun")
print("==========")

# ---------------------------------------------------------------------------
# Ask for a word. .strip() removes any spaces typed before or after it, so
# "  cat  " is treated the same as "cat".
# ---------------------------------------------------------------------------
word = input("Enter a word: ").strip()

# If the user just pressed Enter there is nothing to work with, so use a
# default word instead of printing empty results.
if word == "":
    word = "Python"
    print("(No word entered - using 'Python' instead.)")

print()

# --- Required: length -------------------------------------------------------
# len() counts the characters in a string.
print(f"Length:        {len(word)} characters")

# --- Required: uppercase ----------------------------------------------------
# .upper() returns a new string in capitals; the original is unchanged.
print(f"Uppercase:     {word.upper()}")

# --- Required: repeated three times -----------------------------------------
# The * operator on a string repeats it. Adding a space first keeps the three
# copies readable instead of running them together.
print(f"Repeated x3:   {(word + ' ') * 3}".rstrip())

# --- Extras -----------------------------------------------------------------
print(f"Lowercase:     {word.lower()}")
print(f"Title case:    {word.title()}")
print(f"First letter:  {word[0]}")               # index 0 is the first character
print(f"Last letter:   {word[-1]}")              # index -1 counts from the end
print(f"Reversed:      {word[::-1]}")            # a slice with step -1 reverses it

# A palindrome reads the same forwards and backwards. Comparing the lowercase
# word to its reverse checks that in one line.
if word.lower() == word.lower()[::-1]:
    print(f"Palindrome:    yes, '{word}' reads the same backwards")
else:
    print("Palindrome:    no")
