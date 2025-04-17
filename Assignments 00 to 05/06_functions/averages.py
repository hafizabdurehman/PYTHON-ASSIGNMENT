def find_average(num1, num2):

    """
    This function takes two numbers and returns their average.
    """
    average = (num1 + num2) / 2  # Calculate the average

    return average  # Return the result

# Example usage

num1 = float(input("Enter first number: "))  # Get first number from user

num2 = float(input("Enter second number: "))  # Get second number from user

# Call the function and print the result

print("The average is:", find_average(num1, num2))