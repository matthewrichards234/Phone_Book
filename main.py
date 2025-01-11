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
    favorite = bool(input("Favorite this contact (T/F): "))
    contacts[name] = [phone, address, favorite]

def display_contacts(contacts):
    if not contacts:
        print("You have not added any contacts yet. Please add to your contact list.\n")
    else:
        for contact in contacts:
            print(contact)

def search_contacts(contacts):
    return

def main():
    contacts = {} # Name : Phone, Address, Favorite(T/F)

    menu = display_menu()
    print(menu)

    option = input("What would you like to do: ")

    if option == 1:
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        exit
    else:
        print("Invalid option. Please try again.\n")