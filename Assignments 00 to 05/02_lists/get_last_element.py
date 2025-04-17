from typing import List

def get_last_element(lst: List[str]) -> None:
    """
    This function takes a non-empty list of strings as input and prints the last element.
    """
    print("The last element in the list is:", lst[-1])  # Print the last element

# Prompt user to enter list elements
n: int = int(input("Enter the number of elements in the list: "))

# Create an empty list to store user inputs
user_list: List[str] = []

# Loop to get user input
for i in range(n):
    element: str = input(f"Enter element {i + 1}: ")
    user_list.append(element)  # Add input to list

# Call the function to print the last element
get_last_element(user_list)