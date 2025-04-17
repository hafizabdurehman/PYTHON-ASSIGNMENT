# Constant for the speed of light in m/s
C = 299792458  # Speed of light in meters per second

def main():
    # Read mass in kilograms from the user
    mass_in_kg = float(input("Enter kilos of mass: "))

    # Calculate energy using Einstein's formula: E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)

    # Display the results
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")
    
    # Output the calculated energy in joules
    print(str(energy_in_joules) + " joules of energy!")


if __name__ == '__main__':
    main()
