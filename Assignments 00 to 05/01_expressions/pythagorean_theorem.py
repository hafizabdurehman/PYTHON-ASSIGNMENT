import math  

def main():
    
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse using the Pythagorean theorem
    bc = math.sqrt(ab**2 + ac**2)  

    # Result
    print("The length of BC (the hypotenuse) is:", bc)


if __name__ == '__main__':
    main()
