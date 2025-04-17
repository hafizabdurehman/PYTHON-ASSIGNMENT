def count_even():

    """
    Prompts the user to enter integers until they press enter.
    Counts and prints the number of even numbers entered.
    """
    numbers = []  # List to store user inputs

    while True:

        user_input = input("Enter an integer or press enter to stop: ")  # Get user input
        
        if user_input == "":  # Stop when user presses enter
            break

        try:
            num = int(user_input)  # Convert input to integer
            numbers.append(num)  # Add to list

        except ValueError:

            print("Invalid input. Please enter an integer.")  # Handle non-integer input

    even_count = sum(1 for num in numbers if num % 2 == 0)  # Count even numbers
    
    print(f"Number of even numbers: {even_count}")  # Print the result

# Run the function
count_even()