from typing import List

MAX_LENGTH: int = 3  # Define the maximum length of the list

def shorten(lst: List[str]) -> None:
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed element. If lst is already at or below MAX_LENGTH, it remains unchanged.
    """
    while len(lst) > MAX_LENGTH:
        removed_item: str = lst.pop()  # Remove and store the last element
        print(f"Removed: {removed_item}")  # Print the removed element

def main() -> None:
    """
    Gets a list of user inputs and passes it to the shorten function.
    """
    user_list: List[str] = []
    
    # Get user input for the list
    while True:
        value: str = input("Enter a value (or press Enter to stop): ")
        if value == "":  # Stop collecting input if user presses Enter without input
            break
        user_list.append(value)

    print(f"Original list: {user_list}")
    shorten(user_list)  # Call the shorten function
    print(f"Final list: {user_list}")  # Display the modified list


main()