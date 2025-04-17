def main():
    # Dictionary containing fruits and their prices
    
    fruits = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}
    
    total_cost = 0  # Initialize total cost to 0
    
    # Loop through the dictionary and ask for the quantity of each fruit
    for fruit_name in fruits:
        price = fruits[fruit_name]  # Get the price of the current fruit
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))  # Ask for the quantity
        total_cost += (price * amount_bought)  # Calculate the cost for the current fruit and add to total
    
    # Print the total cost
    print(f"Your total is ${total_cost:.2f}")


if __name__ == '__main__':
    main()
