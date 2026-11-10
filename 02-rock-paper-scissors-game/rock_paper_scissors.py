# import random 

# user_wins = 0
# computer_wins = 0

# options = ["rock", "paper", "scissors"]

# while True:
#     user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
#     if user_input == "q":
#         break
        
#     if user_input not in options:
#         continue
    
#     random_number = random.randint(0, 2)
#     # rock: 0, paper:1, scissors: 2
#     computer_pick = options[random_number]
#     print("Computer picked", computer_pick + ".")
    
#     if user_input == "rock" and computer_pick == "scissors":
#         print("You won!")
#         user_wins += 1
       
#     elif user_input == "paper" and computer_pick == "rock":
#         print("You won!")
#         user_wins += 1
        
#     elif user_input == "scissors" and computer_pick == "paper":
#         print("You won!")
#         user_wins += 1
        
#     else:
#         print("You Lost!")
#         computer_wins += 1
       
# print("You won", user_wins, "times.")
# print("The computer won", computer_wins, "times.")
    
# print("Goodbye! ")
    
    
    

"""
==================================================
          ROCK PAPER SCISSORS GAME
==================================================

Project Number : 02
Language       : Python

Description:
A command-line game where the user plays
Rock, Paper, Scissors against the computer.

Features:
1. Random computer selection
2. Win, loss and draw detection
3. Score tracking
4. Input validation
5. Round counter
6. Final match statistics
7. Replay functionality

Concepts Used:
- Random Module
- Lists
- While Loops
- Conditional Statements
- Functions
- Variables
- User Input

Developer: Ankita Katkar
==================================================
"""

import random


# Available game choices
OPTIONS = ["rock", "paper", "scissors"]


def get_user_choice():
    """Get and validate the user's choice."""

    while True:
        user_input = input(
            "\nChoose Rock, Paper, Scissors (or Q to quit): "
        ).strip().lower()

        if user_input == "q":
            return "q"

        if user_input in OPTIONS:
            return user_input

        print("Invalid choice! Please select Rock, Paper or Scissors.")


def determine_winner(user, computer):
    """Determine the winner of a round."""

    if user == computer:
        return "draw"

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        return "user"

    else:
        return "computer"


def play_game():
    """Run one complete game."""

    user_wins = 0
    computer_wins = 0
    draws = 0
    rounds = 0

    print("\n" + "=" * 40)
    print("       ROCK PAPER SCISSORS")
    print("=" * 40)

    while True:

        user_choice = get_user_choice()

        if user_choice == "q":
            break

        computer_choice = random.choice(OPTIONS)

        rounds += 1

        print("\nYour choice:", user_choice)
        print("Computer choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print("Congratulations! You won this round!")
            user_wins += 1

        elif result == "computer":
            print("Computer won this round!")
            computer_wins += 1

        else:
            print("It's a draw!")
            draws += 1

        print("\n--- SCOREBOARD ---")
        print("Your wins:", user_wins)
        print("Computer wins:", computer_wins)
        print("Draws:", draws)

    # Final match summary
    print("\n" + "=" * 40)
    print("           FINAL RESULTS")
    print("=" * 40)

    print("Total rounds:", rounds)
    print("Your wins:", user_wins)
    print("Computer wins:", computer_wins)
    print("Draws:", draws)

    if user_wins > computer_wins:
        print("\nYou won the overall match!")

    elif computer_wins > user_wins:
        print("\nComputer won the overall match!")

    elif rounds > 0:
        print("\nThe overall match is a tie!")

    else:
        print("\nNo rounds were played.")

    if rounds > 0:
        win_percentage = (user_wins / rounds) * 100
        print(f"Your win percentage: {win_percentage:.2f}%")

    print("\nThanks for playing!")


def main():
    """Main function."""

    while True:
        play_game()

        play_again = input(
            "\nWould you like to play another match? (yes/no): "
        ).strip().lower()

        if play_again not in ("yes", "y"):
            print("\nGoodbye! See you next time.")
            break


if __name__ == "__main__":
    main()
    
