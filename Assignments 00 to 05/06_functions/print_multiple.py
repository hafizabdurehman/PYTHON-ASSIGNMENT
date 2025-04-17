def print_multiple(message, repeats):

    """Prints the message the specified number of times."""

    for _ in range(repeats):  # Loop repeats times

        print(message)

def main():

    """Main function to get user input and call print_multiple."""

    message = input("Please type a message: ")  # Get message from user

    repeats = int(input("Enter a number of times to repeat your message: "))  # Get repeat count
    
    print_multiple(message, repeats)  # Call the function

# Run the program
main()