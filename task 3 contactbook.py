import json

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_contacts(contacts):
    """Save contacts to a JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter the contact name: ")
    phone = input("Enter the contact phone number: ")
    if name in contacts:
        print("Contact already exists. Use a different name.")
    else:
        contacts[name] = phone
        print(f"Contact '{name}' added.")

def view_contacts(contacts):
    """View all contacts."""
    if not contacts:
        print("No contacts available.")
    else:
        print("\nContacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def search_contact(contacts):
    """Search for a contact by name."""
    name = input("Enter the contact name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print(f"Contact '{name}' not found.")

def delete_contact(contacts):
    """Delete a contact by name."""
    name = input("Enter the contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted.")
    else:
        print(f"Contact '{name}' not found.")

def main():
    """Main function to run the contact book."""
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Select an option (1-5): ")

        if choice == '1':
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

