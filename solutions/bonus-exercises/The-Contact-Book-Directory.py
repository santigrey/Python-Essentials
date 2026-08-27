#Scenario: Contact Book Directory
#You are building a simple contact directory. You need to look-up a phone number, update an existing contact, and add a new entry.
#Goal: Access, update, and add key-value pairs inside a dictionary.
#Your Mission
#Create a simple contact directory program called phone_book.
#Look up and print Bob's phone number using his name as the key.
#Alice changed her number. Update her phone number in the dictionary to "555-0000".
#A new person joined. Add "David" to the dictionary with the phone number "555-4321".


phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-8765",
}

# Looking a value up by its key.
print(phone_book["Bob"])

# The key already exists, so assigning to it replaces the old number.
phone_book["Alice"] = "555-0000"

# The key does not exist yet, so this same syntax adds a new pair instead.
phone_book["David"] = "555-4321"

print(phone_book)
