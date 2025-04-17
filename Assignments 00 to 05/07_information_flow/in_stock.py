# Sample inventory dictionary (for demonstration)

inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "pear": 1000,
    "grape": 10
}

def num_in_stock(fruit):

    """Returns the number of a given fruit in stock, or 0 if not found."""

    return inventory.get(fruit.lower(), 0)

def main():

    fruit = input("Enter a fruit: ").strip().lower()

    stock = num_in_stock(fruit)

    if stock > 0:

        print("\nThis fruit is in stock! Here is how many:\n", stock)

    else:
        
        print("\nThis fruit is not in stock.")

# Run the program
main()