# SBA 351 - Contact Book: Interaction Logs

Console output copied from real runs of `SBA-351.py` (Python 3). Everything
after a prompt on the same line is what was typed at the keyboard.

## Session 1 - add, duplicates, view, search, delete, invalid input, exit

Covers: adding two contacts, a rejected exact duplicate, a rejected duplicate
typed in different capitalization, a rejected blank name, a rejected phone
number, viewing the list, a successful search, an unsuccessful search, a
deletion, two invalid menu choices, and a clean exit.

```

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter the contact's name: Alice Johnson
Enter the phone number (digits only): 5551234567
Alice Johnson was added to the contact book.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter the contact's name: Bob Smith
Enter the phone number (digits only): 5559876543
Bob Smith was added to the contact book.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter the contact's name: Alice Johnson
Alice Johnson is already in the contact book. Nothing was changed.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter the contact's name: alice johnson
Alice Johnson is already in the contact book. Nothing was changed.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter the contact's name: 
The name cannot be blank. Nothing was added.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 1
Enter the contact's name: Carol Diaz
Enter the phone number (digits only): 555-1234
'555-1234' is not a valid phone number.
Use digits only, 7 to 15 of them. Nothing was added.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 2
All Contacts:
Alice Johnson: 5551234567
Bob Smith: 5559876543

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 3
Enter a full or partial name to search for: al
Found 1 matching contact(s):
Alice Johnson: 5551234567

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 3
Enter a full or partial name to search for: Zach
No contact matching 'Zach' was found.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 4
Enter the name of the contact to delete: bob smith
Bob Smith was deleted from the contact book.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 2
All Contacts:
Alice Johnson: 5551234567

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): abc
Invalid choice. Please enter a number from 1 to 5.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 9
Invalid choice. Please enter a number from 1 to 5.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 5
Goodbye!
```

## Session 2 - empty contact list

Covers: viewing and searching before any contact exists, and deleting a name
that is not in the book.

```

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 2
The contact list is empty.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 3
The contact list is empty.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 4
Enter the name of the contact to delete: Bob Smith
Bob Smith does not exist in the contact book.

Contact Book Menu:
1. Add New Contact
2. View All Contacts
3. Search Contact
4. Delete Contact
5. Exit
Enter your choice (1-5): 5
Goodbye!
```
