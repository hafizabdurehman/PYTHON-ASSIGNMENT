import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total.
    """
    die1 = random.randint(1, NUM_SIDES)  # Roll the first die
    die2 = random.randint(1, NUM_SIDES)  # Roll the second die
    total = die1 + die2  # Sum the results of both dice
    print("Total of two dice:", total)  # Print the total of the two dice rolls

def main():
    die1 = 10  # This variable is scoped to the main() function
    print("die1 in main() starts as:", die1)
    
    # Simulating three rolls of two dice
    roll_dice()
    roll_dice()
    roll_dice()

    # Printing die1 after the dice rolls
    print("die1 in main() is:", die1)


if __name__ == '__main__':
    main()
