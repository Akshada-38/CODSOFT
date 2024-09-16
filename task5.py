class ContactBook:
    def __init__(self):
        # Dictionary to store contact details (name -> details)
        self.contacts = {}

    # Add a new contact
    def add_contact(self, name, phone, email, address):
        if name in self.contacts:
            print("Contact already exists.")
        else:
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("Contact added successfully.")

    # View the contact list (name and phone number only)
    def view_contacts(self):
        if self.contacts:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"Name: {name}, Phone: {details['phone']}")
        else:
            print("No contacts found.")

    # Search for a contact by name or phone number
    def search_contact(self, search_term):
        found_contacts = []
        for name, details in self.contacts.items():
            if search_term.lower() in name.lower() or search_term in details['phone']:
                found_contacts.append((name, details))
        if found_contacts:
            for name, details in found_contacts:
                print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
        else:
            print("No contact found.")

    # Update an existing contact
    def update_contact(self, name):
        if name in self.contacts:
            print("Enter new details (press Enter to skip updating a field):")
            phone = input(f"New phone number (current: {self.contacts[name]['phone']}): ") or self.contacts[name]['phone']
            email = input(f"New email (current: {self.contacts[name]['email']}): ") or self.contacts[name]['email']
            address = input(f"New address (current: {self.contacts[name]['address']}): ") or self.contacts[name]['address']
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")

    # Delete a contact
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

# Main application logic
def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            contact_book.update_contact(name)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
