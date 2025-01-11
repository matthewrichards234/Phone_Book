def display_menu():
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

def add_contacts(contacts):
    name = input("Please enter the contact's name: ").title()
    phone = input("Enter their phone number: ")
    address = input("Enter their address: ")
    favorite = input("Favorite this contact (T/F): ").strip().lower() == "t"
    contacts[name] = [phone, address, favorite]
    print(f"Contact {name} added successfully!\n")

def display_contacts(contacts):
    if not contacts:
        print("You have not added any contacts yet. Please add to your contact list.\n")
    else:
        print("\nAll Contacts:")
        for name, info in contacts.items():
            phone, address, favorite = info
            favorite_status = "Yes" if favorite else "No"
            print(f"Name: {name}, Phone: {phone}, Address: {address}, Favorite: {favorite_status}")

def search_contacts(contacts):
    name = input("Enter name to search: ").title()
    if name in contacts:
        phone, address, favorite = contacts[name]
        favorite_status = "Yes" if favorite else "No"
        print(f"Name: {name}, Phone: {phone}, Address: {address}, Favorite: {favorite_status}")
    else:
        print(f"No contact found for {name}.\n")

def main():
    contacts = {}  # Dictionary format: {Name: [Phone, Address, Favorite]}

    while True:
        display_menu()
        option = input("Choose an option (1-4): ").strip()

        if option == "1":
            add_contacts(contacts)
        elif option == "2":
            display_contacts(contacts)
        elif option == "3":
            search_contacts(contacts)
        elif option == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
