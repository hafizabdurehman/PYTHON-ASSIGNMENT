import random

# Probability of stopping early

DONE_LIKELIHOOD = 0.3  

def done():

    """
    This function randomly decides whether to stop counting.
    Returns True with probability DONE_LIKELIHOOD.
    """
    return random.random() < DONE_LIKELIHOOD  # Returns True based on probability

def chaotic_counting():

    """
    Prints numbers from 1 to 10, but may stop early based on done() function.
    """
    for i in range(1, 11):  # Loop from 1 to 10

        if done():  # Check if we should stop

            return  # Exit the function early
        
        print(i)  # Print the current number

def main():

    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")

    chaotic_counting()
    
    print("I'm done.")

# Run the program
main()