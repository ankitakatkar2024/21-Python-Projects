# ==========================================
# VERSION 1: Random Number Generation
# ==========================================

# import random
# r =random.randrange(-5, 10)
# r = random.randint(-5, 11)
# print(r)

# ==========================================
# VERSION 2: Basic Number Guessing Game
# ==========================================

# import random
# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)
    
#     if top_of_range <= 0:
#         print("Please type a number larger than 0 next time.")
#         quit()
# else:
#     print("Please type  a number next time.")
#     quit()
    
# random_number = random.randint(0, top_of_range)

# while True:
#   user_guess = input("Make a guess: ")
  
#   if user_guess.isdigit():
#       user_guess = int(user_guess)
    
#   else:
#       print("Please type a valid number.")
#       continue
   
#   if user_guess == random_number:
#       print("You got it!")
#       break
      
#   else:
#       print("You got it wrong! Try again.")          


# ==========================================
# VERSION 3: Guess Counter
# ==========================================

# import random
# top_of_range = input("Type a number: ")

# if top_of_range.isdigit():
#     top_of_range = int(top_of_range)
    
#     if top_of_range <= 0:
#         print("Please type a number larger than 0 next time.")
#         quit()
# else:
#     print("Please type  a number next time.")
#     quit()
    
# random_number = random.randint(0, top_of_range)
# guesses = 0

# while True:
#   guesses += 1
#   user_guess = input("Make a guess: ")
  
#   if user_guess.isdigit():
#       user_guess = int(user_guess)
    
#   else:
#       print("Please type a valid number.")
#       continue
   
#   if user_guess == random_number:
#       print("You got it!")
#       break
#   elif user_guess > random_number:
#           print("You were above the number!")
#   else:
#           print("You were below the number!")

# print("You got it in", guesses, "guesses")          



# ========================================
#         NUMBER GUESSING GAME
# ========================================

# Project: Number Guessing Game
# Language: Python
# Description:
# An interactive guessing game with
# difficulty levels, scoring and
# Features:
# - Three difficulty levels
# - Limited guessing attempts
# - Score calculation
# - High-score tracking
# - JSON file storage
# - Replay functionality
# Developer: Ankita Katkar

# ========================================

import random
import json
from pathlib import Path

# File to store high scores
SCORE_FILE = Path("high_scores.json")

# Difficulty settings
DIFFICULTIES = {
    "1": {"name": "Easy", "limit": 10, "attempts": 5},
    "2": {"name": "Medium", "limit": 50, "attempts": 7},
    "3": {"name": "Hard", "limit": 100, "attempts": 8}
}


def get_high_scores():
    """Load saved high scores."""
    if SCORE_FILE.exists():
        try:
            with SCORE_FILE.open("r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_high_scores(scores):
    """Save high scores to a JSON file."""
    with SCORE_FILE.open("w") as file:
        json.dump(scores, file, indent=4)


def choose_difficulty():
    """Allow the player to select difficulty."""
    print("\nChoose Difficulty:")
    print("1. Easy (0-10)")
    print("2. Medium (0-50)")
    print("3. Hard (0-100)")

    while True:
        choice = input("Enter your choice (1-3): ")

        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]

        print("Invalid choice! Please select 1, 2 or 3.")


def get_guess(limit):
    """Get and validate the user's guess."""
    while True:
        guess = input(f"Enter your guess (0-{limit}): ")

        try:
            guess = int(guess)

            if 0 <= guess <= limit:
                return guess

            print(f"Enter a number between 0 and {limit}.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


def play_game():
    """Run one round of the guessing game."""
    settings = choose_difficulty()

    limit = settings["limit"]
    max_attempts = settings["attempts"]
    difficulty = settings["name"]

    random_number = random.randint(0, limit)

    print(f"\nYou selected {difficulty} mode.")
    print(f"Guess the number between 0 and {limit}.")
    print(f"You have {max_attempts} attempts.\n")

    guesses = 0

    while guesses < max_attempts:
        user_guess = get_guess(limit)
        guesses += 1

        if user_guess == random_number:
            score = max(0, 100 - (guesses - 1) * 10)

            print("\nCongratulations! You guessed correctly!")
            print(f"Attempts used: {guesses}")
            print(f"Your score: {score}")

            return difficulty, score, True

        elif user_guess > random_number:
            print("Too high! Try a smaller number.")

        else:
            print("Too low! Try a bigger number.")

        print(f"Attempts remaining: {max_attempts - guesses}\n")

    print("\nGame over!")
    print(f"The correct number was {random_number}.")

    return difficulty, 0, False


def main():
    """Main function of the application."""
    high_scores = get_high_scores()

    games_played = 0
    games_won = 0

    print("=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)

    while True:
        difficulty, score, won = play_game()

        games_played += 1

        if won:
            games_won += 1

            previous_best = high_scores.get(difficulty, 0)

            if score > previous_best:
                high_scores[difficulty] = score
                save_high_scores(high_scores)
                print("New high score!")

        print("\n--- HIGH SCORES ---")

        for level in ["Easy", "Medium", "Hard"]:
            print(f"{level}: {high_scores.get(level, 0)}")

        print("\n--- GAME STATISTICS ---")
        print(f"Games played: {games_played}")
        print(f"Games won: {games_won}")

        play_again = input("\nPlay again? (yes/no): ").strip().lower()

        if play_again not in ("yes", "y"):
            break

    print("\nThank you for playing!")
    print("Final games played:", games_played)
    print("Final games won:", games_won)


if __name__ == "__main__":
    main()

  
  
  