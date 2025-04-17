MINIMUM_HEIGHT: int = 50  # Arbitrary units for height (can be inches, centimeters, etc.)

def main():
    
    height = float(input("How tall are you? "))  # Convert the input into a float for precise height measurement
    
    # Check if the user is tall enough to ride
    if height >= MINIMUM_HEIGHT:

        print("You're tall enough to ride!")  # Output if user is tall enough

    else:
        print("You're not tall enough to ride, but maybe next year!") 



if __name__ == '__main__':
    main()
