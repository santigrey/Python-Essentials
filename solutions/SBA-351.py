#SBA 351: Contact Book Program
#(The assignment names the file contact_book.py; it is saved here as SBA-351.py
#to match the naming used for the other SBAs in this repo.)
#Goal: Build a menu-driven command-line contact book using a dictionary.
#Your Mission
#Add New Contact - ask for a name and phone number and store them in a dictionary
#(key: name, value: phone number). Reject duplicate names and invalid phone numbers.
#View All Contacts - print every name and number, or "The contact list is empty."
#Search Contact - look up a full or partial name and show any matches.
#Delete Contact - remove a contact if it exists, otherwise say that it does not.
#Exit - end the program.
#The menu repeats after every action except exit, each feature lives in its own
#function that takes the contacts dictionary, and try/except guards bad input.


# A phone number has to be digits only and fall inside this length range.
MIN_PHONE_DIGITS = 7
MAX_PHONE_DIGITS = 15


# ---------------------------------------------------------------------------
# Small helper functions. Each one returns a value so the feature functions
# below can stay short and none of the same logic gets written twice.
# ---------------------------------------------------------------------------

def is_valid_phone(number):
    """Return True only for a digits-only number of a reasonable length."""
    if not number.isdigit():
        return False
    return MIN_PHONE_DIGITS <= len(number) <= MAX_PHONE_DIGITS


def find_existing_name(contacts, name):
    """Return the stored spelling of a name, ignoring case, or None if unused.

    Looking the name up this way means "bob smith" and "Bob Smith" are treated
    as the same person, so the same contact cannot be stored twice.
    """
    for existing_name in contacts:
        if existing_name.lower() == name.lower():
            return existing_name
    return None


def find_matches(contacts, term):
    """Return a dictionary of the contacts whose name contains term.

    Lowercasing both sides makes the search ignore capitalization, and the "in"
    operator matches a partial name as well as an exact one.
    """
    matches = {}
    for name in sorted(contacts):
        if term.lower() in name.lower():
            matches[name] = contacts[name]
    return matches


def contact_list_is_empty(contacts):
    """Print a message and return True when no contacts are stored yet."""
    # An empty dictionary is falsy, so this catches the "no contacts yet" case.
    if not contacts:
        print("The contact list is empty.")
        return True
    return False


def print_contact(name, phone):
    """Print one contact in the standard name/number format."""
    print(f"{name}: {phone}")


# ---------------------------------------------------------------------------
# The four menu features. Each takes the contacts dictionary as a parameter.
# ---------------------------------------------------------------------------

def add_contact(contacts):
    """Add one new name and number to the dictionary."""
    name = input("Enter the contact's name: ").strip()

    if name == "":
        print("The name cannot be blank. Nothing was added.")
        return

    # Assigning to a key that already exists would silently overwrite the old
    # number, so the duplicate is turned away before that can happen.
    existing_name = find_existing_name(contacts, name)
    if existing_name is not None:
        print(f"{existing_name} is already in the contact book. Nothing was changed.")
        return

    phone = input("Enter the phone number (digits only): ").strip()

    if not is_valid_phone(phone):
        print(f"'{phone}' is not a valid phone number.")
        print(f"Use digits only, {MIN_PHONE_DIGITS} to {MAX_PHONE_DIGITS} of them."
              " Nothing was added.")
        return

    contacts[name] = phone
    print(f"{name} was added to the contact book.")


def view_contacts(contacts):
    """Print every contact in the dictionary."""
    if contact_list_is_empty(contacts):
        return

    print("All Contacts:")
    # Optional enhancement: sorted() lists the names alphabetically.
    for name in sorted(contacts):
        print_contact(name, contacts[name])


def search_contact(contacts):
    """Find and print the contacts whose name contains the text the user typed."""
    if contact_list_is_empty(contacts):
        return

    term = input("Enter a full or partial name to search for: ").strip()

    if term == "":
        print("Please enter something to search for.")
        return

    matches = find_matches(contacts, term)

    if not matches:
        print(f"No contact matching '{term}' was found.")
        return

    print(f"Found {len(matches)} matching contact(s):")
    for name in matches:
        print_contact(name, matches[name])


def delete_contact(contacts):
    """Remove a contact from the dictionary by name."""
    name = input("Enter the name of the contact to delete: ").strip()

    # find_existing_name lets the user delete a contact without having to match
    # the capitalization they originally typed.
    existing_name = find_existing_name(contacts, name)

    if existing_name is None:
        print(f"{name} does not exist in the contact book.")
        return

    del contacts[existing_name]
    print(f"{existing_name} was deleted from the contact book.")


# ---------------------------------------------------------------------------
# The menu itself.
# ---------------------------------------------------------------------------

def show_menu():
    """Print the menu options."""
    print()
    print("Contact Book Menu:")
    print("1. Add New Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def get_choice():
    """Ask for a menu number and return it, or 0 if the answer was not a number."""
    try:
        return int(input("Enter your choice (1-5): "))
    except ValueError:
        # int() raises ValueError on text like "abc". 0 is never a valid menu
        # option, so main() reports the error and shows the menu again.
        return 0


def main():
    """Run the menu loop until the user chooses to exit."""
    contacts = {}

    while True:
        show_menu()
        choice = get_choice()

        if choice == 1:
            add_contact(contacts)
        elif choice == 2:
            view_contacts(contacts)
        elif choice == 3:
            search_contact(contacts)
        elif choice == 4:
            delete_contact(contacts)
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


# Ctrl+C or the end of piped input would otherwise end the program with a
# traceback, so they are caught here and turned into a normal goodbye.
try:
    main()
except (EOFError, KeyboardInterrupt):
    print()
    print("Input ended. Goodbye!")
