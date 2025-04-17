def get_user_data():

    """Asks for user details and returns them as a tuple."""

    first_name = input("What is your first name?: ").strip()

    last_name = input("What is your last name?: ").strip()

    email = input("What is your email address?: ").strip()

    return first_name, last_name, email  # Returns a tuple with user data

def main():

    user_data = get_user_data()
    
    print("\nReceived the following user data:", user_data)

# Run the program
main()