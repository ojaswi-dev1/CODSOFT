# CONTACT BOOK - TASK 5


import json
import os

# File where contacts will be stored permanently
FILE_PATH = "contacts.json"


# ---------------------------- FILE HANDLING ---------------------------- #

def load_contacts():
    """Load contacts from JSON file."""
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)


def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(FILE_PATH, "w") as f:
        json.dump(contacts, f, indent=4)


# Load existing contacts at program start
contacts = load_contacts()


# ---------------------------- FEATURES ---------------------------- #

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
        return

    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. {contact['name']} - {contact['phone']}")


def search_contact():
    print("\n--- Search Contact ---")
    keyword = input("Enter name or phone: ")

    found = [c for c in contacts if keyword.lower() in c["name"].lower() or keyword in c["phone"]]

    if not found:
        print("No matching contacts found.")
        return

    print(f"\nFound {len(found)} contact(s):")
    for contact in found:
        print("\nName   :", contact["name"])
        print("Phone  :", contact["phone"])
        print("Email  :", contact["email"])
        print("Address:", contact["address"])


def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter the name of the contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("\nLeave blank to keep existing value.")

            new_name = input(f"New name ({contact['name']}): ")
            new_phone = input(f"New phone ({contact['phone']}): ")
            new_email = input(f"New email ({contact['email']}): ")
            new_address = input(f"New address ({contact['address']}): ")

            if new_name.strip(): contact["name"] = new_name
            if new_phone.strip(): contact["phone"] = new_phone
            if new_email.strip(): contact["email"] = new_email
            if new_address.strip(): contact["address"] = new_address

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")


# ---------------------------- MAIN MENU ---------------------------- #

def main_menu():
    while True:
        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==================================")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1–6.")


# Run program
if __name__ == "__main__":
    main_menu()
