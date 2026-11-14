
def parse_input(user_input):
    """Split the input into a lowercase command and a list of arguments."""
    try:
        cmd, *args = user_input.split()
    except ValueError:  # empty input
        return "", []
    return cmd.lower(), args

def add_contact(args, contacts):
    """Add a contact. 
    
    Format: add [name] [phone]
    """
    if len(args) != 2:
        return "Please enter: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """Change the phone of an existing contact.

    Format: change [name] [phone]
    """
    if len(args) != 2:
        return "Please enter: change [name] [phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact doesn't exist."
def show_phone(args, contacts):
    """Return the phone of a contact.

    Format: phone [name]
    """
    if len(args) != 1:
        return "Please enter: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact doesn't exist."

def show_all(contacts):
    """Returns all contacts

    Format: all
    """
    if not contacts:
        return "No contacts."
    return "\n".join(f"{name} : {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()