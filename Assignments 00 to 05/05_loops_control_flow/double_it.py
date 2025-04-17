# Ask the user to enter a number

curr_value = int(input("Enter a number: "))  # Convert input to an integer

# Loop to keep doubling the number until it reaches or exceeds 100

while curr_value < 100:

    curr_value = curr_value * 2  # Double the value
    
    print(curr_value)  # Print the updated value