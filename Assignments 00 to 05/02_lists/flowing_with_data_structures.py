def add_three_copies(lst: list[str], data: str) -> None:
    """
    This function takes a list of strings and a data value (string), 
    then adds three copies of the data to the list. It modifies the list directly.
    """
    lst.append(data)  # Add first copy of data
    lst.append(data)  # Add second copy of data
    lst.append(data)  # Add third copy of data

# Ask user for input
message: str = input("Enter a message to copy: ")

# Create an empty list to store the copies
my_list: list[str] = []

# Print the list before modification
print("List before:", my_list)

# Call the function to add three copies of the user input
add_three_copies(my_list, message)

# Print the list after modification to show the effect of mutability
print("List after:", my_list)