def mad_libs():
    print("Welcome to the Mad Libs game! Fill in the blanks below:")

    # Collect user inputs
    name = input("Enter a name: ")

    place = input("Enter a place: ")

    animal = input("Enter an animal: ")

    food = input("Enter a type of food: ")

    emotion = input("Enter an emotion: ")

    verb = input("Enter a verb: ")

    adjective = input("Enter an adjective: ")

    # Create the Mad Libs story using f-strings

    story = f"""
    Once upon a time, {name} went on an adventure to {place}.
    There, they encountered a {adjective} {animal} who was very {emotion}.
    To calm the {animal}, {name} decided to {verb} and offer it some {food}.
    Surprisingly, the {animal} loved it and became {name}'s best friend.
    And so, {name} and the {animal} lived happily ever after. The end!
    """

    # Print the completed story

    print("\nHere’s your Mad Libs story:\n")
    
    print(story)

# Run the game
mad_libs()