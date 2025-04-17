# Define the correct affirmation

affirmation = "I am capable of doing anything I put my mind to."

# Loop until the user types the correct affirmation

while True:
    # Prompt the user for input

    user_input = input("Please type the following affirmation: ")

    # Check if the input matches the affirmation

    if user_input == affirmation:

        print("That's right! :)")  # Success message

        break  # Exit the loop

    else:
        print("Hmmm, that was not the affirmation. Try again.")  # Error message