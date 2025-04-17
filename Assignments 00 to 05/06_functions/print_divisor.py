def print_divisors(num):

    """Prints all divisors of the given number."""

    print(f"Here are the divisors of {num}")

    for i in range(1, num + 1):  # Loop from 1 to num

        if num % i == 0:  # Check if i is a divisor of num

            print(i, end=" ")  # Print the divisor

def main():

    """Main function to get user input and call print_divisors."""

    num = int(input("Enter a number: "))  # Get user input
    
    print_divisors(num)  # Call the helper function

# Run the program
main()