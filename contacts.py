
def add_contacts(contact_name, contact_email, contact_number):
    contact = {"Name": contact_name, "Email": contact_email, "Number": contact_number}
    contacts.append(contact)
    print(f"{contact_name} is now on your contact List.\n")
    return

def show_contacts():
    print("\nMy contact List:")
    if not contacts:
        print("The contact list is empty.\n")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. Name: {contact['Name']}, Email: {contact['Email']}, Number: {contact['Number']}")
    print()
    return

def update_contacts(contact_name, new_email, new_number):
    for contact in contacts:
        if contact["Name"].lower() == contact_name.lower():
            contact["Email"] = new_email
            contact["Number"] = new_number
            print(f"Contact {contact_name} uptaded sucefully!! .\n")
            return
    print(f"Contact {contact_name} does not exist.\n")
    return

def delete_contact(contact_name):
    for contact in contacts:
        if contact["Name"].lower() == contact_name.lower():
            contacts.remove(contact)
            print(f"Contact {contact_name} has been removed .\n")
            return
    print(f"Contact {contact_name} does not exist.\n")
    return

contacts = []
while True:
    print("Menu")
    print("1. Add contact")
    print("2. Show contacts")
    print("3. Update contact")
    print("4. Remove contact")
    print("5. Close contact List")
    option = input("Select an option: ")

    if option == "1":
        contact_name = input("Name: ")
        contact_email = input("Email: ")
        contact_number = input("Number: ")
        add_contacts(contact_name, contact_email, contact_number)

    elif option == "2":
        show_contacts()

    elif option == "3":
        contact_name = input(": ")
        new_email = input("New Email: ")
        new_number = input("New Number: ")
        update_contacts(contact_name, new_email, new_number)

    elif option == "4":
        contact_name = input("Name:  ")
        delete_contact(contact_name)

    elif option == "5":
        print("You close your contact List, bye.")
        break

    else:
        print("try again.\n")
