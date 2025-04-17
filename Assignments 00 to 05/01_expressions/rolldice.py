import random 

# Number of sides on each die
NUM_SIDES = 6

def main():
    # Roll the dice
    die1 = random.randint(1, NUM_SIDES)  # Random number between 1 and 6 for the first die
    die2 = random.randint(1, NUM_SIDES)  # Random number between 1 and 6 for the second die
    
    # Calculate the total sum of the dice rolls
    total = die1 + die2
    
    # Results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)


if __name__ == '__main__':
    main()
