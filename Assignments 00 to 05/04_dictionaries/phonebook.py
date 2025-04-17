def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the phonebook.
    """
    phonebook = {}  # Create an empty phonebook (dictionary)

    while True:
        name = input("Name: ")
        if name == "":  # If user presses Enter without typing a name, exit the loop
            break
        number = input("Number: ")
        phonebook[name] = number  # Store the name as a key and the number as the value

    return phonebook

def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    if phonebook:
        for name in phonebook:
            print(f"{name} -> {phonebook[name]}")  # Print each name and its corresponding number
    else:
        print("The phonebook is empty.")

def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers in the phonebook by entering a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":  # If user presses Enter without typing a name, exit the loop
            break
        if name not in phonebook:
            print(f"{name} is not in the phonebook.")  # If name isn't found, inform the user
        else:
            print(phonebook[name])  # Print the phone number if name is found

def main():
    """
    Main function that reads phone numbers, prints the phonebook, and allows lookups.
    """
    phonebook = read_phone_numbers()  # Call function to read phone numbers
    print_phonebook(phonebook)         # Call function to print the phonebook
    lookup_numbers(phonebook)         # Call function to allow lookup of phone numbers


if __name__ == '__main__':
    main()
