def greet(name):

    """Prints a greeting message."""

    print(f"Greetings {name}!")

def main():

    """Gets the user's name and greets them."""

    name = input("What's your name? ")  # Get user input
    
    greet(name)  # Call the helper function to greet

# Run the program
main()