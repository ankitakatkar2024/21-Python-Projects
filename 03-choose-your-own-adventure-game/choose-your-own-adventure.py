#  Basic Adventure Game 

# name = input("Type your name: ")
# print(f"Welcome, {name}, to the adventure game!")

# answer = input(
#     "You are on a dirt road. It has come to an end and you can go left or right. Which way would you like to go? "
# ).lower()

# if answer == "left":

#     answer = input(
#         "You come to a river. You can walk around it or swim across. Type walk or swim: "
#     ).lower()

#     if answer == "swim":
#         print("You swim across, but you are eaten by an alligator. Game Over.")

#     elif answer == "walk":
#         print("You walk for many miles, run out of water, and lose the game.")

#     else:
#         print("Not a valid option. Please choose walk or swim.")

# elif answer == "right":

#     answer = input(
#         "You come to a bridge. It looks wobbly. Do you want to cross it or head back? (cross/back): "
#     ).lower()

#     if answer == "back":
#         print("You go back and lose the game.")

#     elif answer == "cross":

#         answer = input(
#             "You cross the bridge and meet a stranger. Do you want to talk to them? (yes/no): "
#         ).lower()

#         if answer == "yes":
#             print("You talk to the stranger. They give you directions to the nearest town. You win!")

#         elif answer == "no":
#             print("You ignore the stranger and continue on your way, but you get lost in the forest. Game Over.")

#         else:
#             print("Not a valid option. Please choose yes or no.")

#     else:
#         print("Not a valid option. Please choose cross or back.")

# else:
#     print("Not a valid option. Please choose left or right.")

# print("THANK YOU FOR PLAYING!")



"""
Project 03: Adventure Game
Language: Python
Description: A text-based adventure game where users make
choices and experience different outcomes.
Developer: Ankita Katkar
"""

def get_choice(prompt, valid_options):
    """Get and validate the user's choice."""

    while True:
        answer = input(prompt).strip().lower()

        if answer in valid_options:
            return answer

        print(f"Invalid choice! Please choose from: {', '.join(valid_options)}")


def play_game():
    """Run one round of the adventure game."""

    print("\n" + "=" * 40)
    print("       WELCOME TO THE ADVENTURE")
    print("=" * 40)

    name = input("\nEnter your name: ").strip()

    if not name:
        name = "Adventurer"

    print(f"\nWelcome, {name}! Your adventure begins now.")

    answer = get_choice(
        "\nYou are standing on a dirt road. "
        "It ends here. You can go left or right.\n"
        "Choose left or right: ",
        ["left", "right"]
    )

    if answer == "left":

        answer = get_choice(
            "\nYou reach a river. You can walk around it "
            "or swim across it.\nChoose walk or swim: ",
            ["walk", "swim"]
        )

        if answer == "swim":
            print("\nYou swim across the river, but an alligator attacks you.")
            print("GAME OVER!")

        else:
            print("\nYou walk for many miles, run out of water, and collapse.")
            print("GAME OVER!")

    else:

        answer = get_choice(
            "\nYou reach a wobbly bridge. Do you want to cross it or go back?\n"
            "Choose cross or back: ",
            ["cross", "back"]
        )

        if answer == "back":
            print("\nYou turn back and lose your way.")
            print("GAME OVER!")

        else:

            answer = get_choice(
                "\nYou cross the bridge and meet a stranger. "
                "Do you want to talk to them?\nChoose yes or no: ",
                ["yes", "no"]
            )

            if answer == "yes":
                print("\nThe stranger gives you directions to the nearest town.")
                print("You reach the town safely. YOU WIN!")

            else:
                print("\nYou ignore the stranger and enter a forest.")
                print("You get lost in the forest. GAME OVER!")


def main():
    """Start and manage the game."""

    while True:
        play_game()

        replay = get_choice(
            "\nWould you like to play again? (yes/no): ",
            ["yes", "no"]
        )

        if replay == "no":
            print("\nThank you for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()

