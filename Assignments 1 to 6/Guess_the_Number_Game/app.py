import random

def guess_the_number():

    print("🎯 Welcome to the Guess the Number Game!")
    
    # Generate a random number between 1 and 100

    secret_number = random.randint(1, 10)

    attempts = 0
    
    while True:

        try:
            # Get user input and convert it to an integer
            guess = int(input("Enter your guess (1-10): "))
            
            # Increase attempt count
            attempts += 1

            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again.")

            elif guess > secret_number:
                print("Too high! Try again.")
                
            else:
                print(f"🎉 Congrats! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the loop when guessed correctly
        
        except ValueError:
            print("⚠️ Please enter a valid number between 1 and 10.")

# Run the game
guess_the_number()