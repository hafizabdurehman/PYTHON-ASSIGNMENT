def main():
    # Get the numbers we want to divide
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))

    # Perform integer division and get the quotient
    quotient = dividend // divisor  
    
    # Get the remainder using the modulo operator
    remainder = dividend % divisor 
    
    # Result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
