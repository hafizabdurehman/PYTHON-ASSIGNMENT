def print_ones_digit(num):

    """Prints the ones digit of the given number."""

    ones_digit = num % 10  # Get the ones digit using modulo operator

    print(f"The ones digit is {ones_digit}")

def main():

    """Main function to get user input and call print_ones_digit."""

    num = int(input("Enter a number: "))  # Get an integer from the user
    
    print_ones_digit(num)  # Call the function

# Run the program
main()