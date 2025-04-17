def subtract_seven(num):

    """Subtracts 7 from num and returns the result."""

    return num - 7

def main():

    number = int(input("Enter a number: "))  # Get user input

    result = subtract_seven(number)  # Call the helper function
    
    print("Result after subtracting 7:", result)  # Print the result

# Run the program
main()