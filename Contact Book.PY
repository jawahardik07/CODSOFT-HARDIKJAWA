import json

# File to store contacts
FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact {name} added successfully!")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    
    print("\nContact List:")
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}")
    print()

# Search for a contact by name or phone number
def search_contact(contacts):
    search_term = input("Enter the name or phone number to search: ").lower()
    found_contacts = [contact for contact in contacts if search_term in contact["name"].lower() or search_term in contact["phone"]]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            print("-" * 20)
    else:
        print("No contacts found.")

# Update an existing contact
def update_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to update: ")) - 1

    if 0 <= index < len(contacts):
        contact = contacts[index]
        print(f"Updating contact: {contact['name']}")

        contact["name"] = input(f"Enter new name (or press enter to keep '{contact['name']}'): ") or contact["name"]
        contact["phone"] = input(f"Enter new phone number (or press enter to keep '{contact['phone']}'): ") or contact["phone"]
        contact["email"] = input(f"Enter new email (or press enter to keep '{contact['email']}'): ") or contact["email"]
        contact["address"] = input(f"Enter new address (or press enter to keep '{contact['address']}'): ") or contact["address"]

        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

# Delete a contact
def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter the contact number to delete: ")) - 1

    if 0 <= index < len(contacts):
        contact = contacts.pop(index)
        save_contacts(contacts)
        print(f"Contact {contact['name']} deleted successfully!")
    else:
        print("Invalid contact number.")

# Main program loop
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. View Contact List")
        print("2. Add New Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
