import csv
import os

FILENAME = "contacts.csv"

# Load contacts from CSV file
def load_contacts():
    contacts = []
    if os.path.exists(FILENAME):
        with open(FILENAME, newline='') as file:
            reader = csv.DictReader(file)
            contacts = list(reader)
    return contacts

# Save contacts to CSV file
def save_contacts(contacts):
    with open(FILENAME, 'w', newline='') as file:
        fieldnames = ['name', 'phone', 'email', 'address']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    save_contacts(contacts)
    print("Contact added and saved.\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
    else:
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

def search_contact(contacts):
    query = input("Enter name or phone to search: ")
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    for contact in results:
        print(contact)
    if not results:
        print("No match found.\n")

def update_contact(contacts):
    view_contacts(contacts)
    user_input = input("Enter contact number to update: ")
    if not user_input.isdigit():
        print("Please enter a valid number.")
        return
    idx = int(user_input) - 1
    if 0 <= idx < len(contacts):
        contacts[idx]['name'] = input("New name: ")
        contacts[idx]['phone'] = input("New phone: ")
        contacts[idx]['email'] = input("New email: ")
        contacts[idx]['address'] = input("New address: ")
        save_contacts(contacts)
        print("Contact updated and saved.\n")
    else:
        print("Invalid contact number.\n")


def delete_contact(contacts):
    view_contacts(contacts)
    idx = int(input("Enter contact number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        del contacts[idx]
        save_contacts(contacts)
        print("Contact deleted.\n")
    else:
        print("Invalid selection.\n")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

if __name__ == "__main__":
    main()
