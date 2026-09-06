# ALAB 356.2 - Task 1: String Manipulation Challenge
# Asks for a sentence, then shows it uppercased, reversed, its vowel count,
# and with every space swapped for a hyphen.

sentence = input("Enter a sentence: ")

# .upper() returns a new string; it does not change the original.
print("Uppercase:", sentence.upper())

# [::-1] is a slice with a step of -1, which walks the string backwards.
print("Reversed:", sentence[::-1])

# Count the vowels. Lowercasing the character first means one check covers
# both "A" and "a".
vowel_count = 0
for character in sentence:
    if character.lower() in "aeiou":
        vowel_count += 1

print("Vowel Count:", vowel_count)

# .replace() swaps every occurrence, not just the first one.
print("Spaces Replaced:", sentence.replace(" ", "-"))
