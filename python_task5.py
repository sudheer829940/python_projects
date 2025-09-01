# Contact Book Application
# Task 5 - CodSoft Internship (Python)

contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!\n")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.\n")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")
    print()

def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone to search: ").strip().lower()
    found = False
    for contact in contacts:
        if keyword in contact['name'].lower() or keyword in contact['phone']:
            print("Name:", contact['name'])
            print("Phone:", contact['phone'])
            print("Email:", contact['email'])
            print("Address:", contact['address'])
            print()
            found = True
    if not found:
        print("No matching contact found.\n")

def update_contact():
    print("\n--- Update Contact ---")
    search_name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            print("Leave blank if you don't want to change.")
            new_phone = input(f"New Phone ({contact['phone']}): ").strip()
            new_email = input(f"New Email ({contact['email']}): ").strip()
            new_address = input(f"New Address ({contact['address']}): ").strip()

            if new_phone:
                contact['phone'] = new_phone
            if new_email:
                contact['email'] = new_email
            if new_address:
                contact['address'] = new_address

            print("Contact updated successfully!\n")
            return
    print("Contact not found.\n")

def delete_contact():
    print("\n--- Delete Contact ---")
    search_name = input("Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == search_name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return
    print("Contact not found.\n")

def main():
    while True:
        print("===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
