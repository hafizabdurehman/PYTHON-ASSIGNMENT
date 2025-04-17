from typing import List

def collect_user_inputs() -> List[str]:
    """
    Continuously prompts the user for input and adds values to a list.
    Stops collecting input when the user presses Enter without typing anything.
    Returns the final list of inputs.
    """
    user_list: List[str] = []  # Initialize an empty list

    while True:
        value: str = input("Enter a value: ")
        if value == "":  # Stop when the user presses Enter without typing anything
            break
        user_list.append(value)  # Add the entered value to the list

    return user_list

# Call the function and display the collected list
final_list: List[str] = collect_user_inputs()
print("Here's the list:", final_list)