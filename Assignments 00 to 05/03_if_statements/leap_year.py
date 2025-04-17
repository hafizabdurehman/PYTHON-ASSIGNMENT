def main():
    # Get the year from the user
    year = int(input('Please input a year: '))

    # Check if the year is divisible by 4
    if year % 4 == 0:

        # Check if the year is also divisible by 100
        if year % 100 == 0:

            # Check if the year is divisible by 400
            if year % 400 == 0:
                print("That's a leap year!")  # Divisible by 400

            else:
                print("That's not a leap year.")  # Divisible by 100 but not 400

        else:
            print("That's a leap year!")  # Divisible by 4 but not by 100

    else:
        print("That's not a leap year.")  # Not divisible by 4



if __name__ == '__main__':
    main()
