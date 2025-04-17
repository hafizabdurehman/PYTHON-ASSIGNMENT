import random  # Importing the random module to generate a random number

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# Infinite loop until the user guesses correctly
while True:
    try:
        # Ask user for a guess and convert it to an integer
        guess = int(input("Enter a guess: "))

        # Check if the guess is too high, too low, or correct
        if guess > secret_number:
            print("Your guess is too high\n")
        elif guess < secret_number:
            print("Your guess is too low\n")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit the loop when the guess is correct
    except ValueError:
        print("Invalid input! Please enter a number between 0 and 99.\n")