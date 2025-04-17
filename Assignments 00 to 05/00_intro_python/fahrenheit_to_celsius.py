def main():
    
    # Temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    
    # Convert the temperature from Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    
    # Result
    print("Temperature: " + str(fahrenheit) + "F = " + str(celsius) + "C")



if __name__ == '__main__':
    main()