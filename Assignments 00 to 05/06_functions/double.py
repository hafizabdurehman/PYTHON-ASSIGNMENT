def double(num):

    """
    Returns the result of multiplying num by 2.
    """
    return num * 2

def main():

    """
    Prompts the user for a number, calls double(num),
    and prints the result.
    """
    num = int(input("Enter a number: "))  # Get user input and convert to integer

    result = double(num)  # Call the double function
    
    print(f"Double that is {result}")  # Print the result

# Run the program
main()