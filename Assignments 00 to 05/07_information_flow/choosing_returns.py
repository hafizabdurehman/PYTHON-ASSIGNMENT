# Define the legal adult age in the U.S.
ADULT_AGE = 18  

def is_adult(age):

    """Returns True if age is greater than or equal to ADULT_AGE, otherwise False."""

    return age >= ADULT_AGE  

def main():

    """Main function to get user input and check if they are an adult."""

    age = int(input("How old is this person?: "))  # Get the age as input
    
    print(is_adult(age))  # Call is_adult and print the result

# Run the program
main()