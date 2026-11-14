
# import random


# def roll():
#     min_value = 1
#     max_value = 6
#     value = random.randint(min_value, max_value)
#     return value


# # Get number of players
# while True:
#     players = input("Enter the number of players (2-4): ")

#     if players.isdigit():
#         players = int(players)

#         if 2 <= players <= 4:
#             break
#         else:
#             print("Must be a number between 2 and 4.")

#     else:
#         print("Please enter a valid number.")


# # Game settings
# max_score = 50
# player_scores = [0 for _ in range(players)]


# # Main game loop
# while max(player_scores) < max_score:

#     for player_idx in range(players):

#         print("\nPlayer number", player_idx + 1, "turn has just started!\n")
#         print("Your total score is:", player_scores[player_idx], "\n")

#         current_score = 0

#         while True:
#             should_roll = input("Would you like to roll (y)? ")

#             if should_roll.lower() != "y":
#                 break

#             value = roll()

#             if value == 1:
#                 print("You rolled a 1! Turn done!")
#                 current_score = 0
#                 break

#             else:
#                 current_score += value
#                 print("You rolled a:", value)

#             print("Your current score is:", current_score)

#         # Update total score
#         player_scores[player_idx] += current_score

#         print("Your total score is:", player_scores[player_idx])

#         # Check if player wins
#         if player_scores[player_idx] >= max_score:
#             break


# # Display final scores
# print("\nFinal Scores:")

# for player_idx, score in enumerate(player_scores):
#     print("Player", player_idx + 1, ":", score)


# # Display winner
# max_score = max(player_scores)
# winning_idx = player_scores.index(max_score)

# print(
#     "\nPlayer number", winning_idx + 1,
#     "is the winner with a score of:", max_score
# )


import random


def roll():
    return random.randint(1, 6)


def get_players():
    while True:
        players = input("Enter the number of players (2-4): ").strip()

        if players.isdigit() and 2 <= int(players) <= 4:
            return int(players)

        print("Please enter a valid number between 2 and 4.")


def play_game():
    max_score = 50
    players = get_players()

    player_scores = [0 for _ in range(players)]

    while max(player_scores) < max_score:

        for player_idx in range(players):

            print("\n" + "=" * 40)
            print(f"Player {player_idx + 1}'s turn")
            print(f"Total score: {player_scores[player_idx]}")
            print("=" * 40)

            current_score = 0

            while True:
                choice = input("Roll the dice? (y/n): ").lower().strip()

                if choice == "n":
                    print("\nTurn ended!")
                    player_scores[player_idx] += current_score
                    break

                elif choice != "y":
                    print("Invalid choice. Enter y or n.")
                    continue

                value = roll()
                print(f"You rolled: {value}")

                if value == 1:
                    print("Oops! You rolled a 1.")
                    print("Your turn score is lost!")

                    current_score = 0
                    break

                current_score += value

                print(f"Current turn score: {current_score}")

            print(f"Player {player_idx + 1} total score: "
                  f"{player_scores[player_idx]}")

            if player_scores[player_idx] >= max_score:
                print("\n" + "*" * 40)
                print(f"Player {player_idx + 1} wins the game!")
                print("*" * 40)
                return

    print("\nFinal Scores:")

    for player_idx, score in enumerate(player_scores):
        print(f"Player {player_idx + 1}: {score}")


# Main program
while True:
    play_game()

    replay = input("\nWould you like to play again? (y/n): ").lower().strip()

    if replay != "y":
        print("\nThank you for playing Pig Dice Game!")
        break
