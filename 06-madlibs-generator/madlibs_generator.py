
# ==========================================
# PROJECT 06: MAD LIBS GENERATOR
# ==========================================
# A fun word game that creates funny stories
# using words entered by the user.
# ==========================================


def madlibs():

    print("\n================================")
    print("       MAD LIBS GENERATOR")
    print("================================")

    print("\nEnter the following words to create your story!\n")

    # Taking user inputs
    name = input("Enter a person's name: ")
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    animal = input("Enter an animal: ")
    food = input("Enter a type of food: ")
    verb = input("Enter a verb: ")
    number = input("Enter a number: ")
    emotion = input("Enter an emotion: ")
    object_name = input("Enter an object: ")

    # Creating the story
    story = f"""
    One day, {name} went to {place}.

    It was a very {adjective} day.

    Suddenly, a {animal} appeared and started eating
    {food}!

    {name} decided to {verb} {number} times to scare
    the animal.

    But the animal was not {emotion} at all.

    Instead, it picked up a {object_name} and ran away!

    What a crazy day at {place}!
    """

    # Displaying the final story
    print("\n================================")
    print("          YOUR STORY")
    print("================================")

    print(story)


# Main program
while True:

    madlibs()

    play_again = input(
        "\nWould you like to create another story? (y/n): "
    ).lower().strip()

    if play_again != "y":
        print("\nThank you for playing Mad Libs!")
        break
