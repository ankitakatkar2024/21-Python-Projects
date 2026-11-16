# Basic Version 

from pathlib import Path

story_path = Path(__file__).parent / "story.txt"

with open(story_path, "r") as f:
    story = f.read()

print(story)
with open("story.txt","r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i
        
    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1
        
# print("Words to replace:", words)
answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer
# print(answers)

for word in words:
     story = story.replace(word, answers[word])

print(story)
     


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


# Advanced version3 

from pathlib import Path
import re

# Get the folder where this Python file is located
BASE_DIR = Path(__file__).parent

# Available languages and their story files
languages = {
    "1": {
        "name": "English",
        "file": "story.txt",
        "prompts": {
            "adjective": "Enter an adjective: ",
            "place": "Enter a place: ",
            "animal": "Enter an animal: ",
            "emotion": "Enter an emotion: ",
            "object": "Enter an object: ",
            "character": "Enter a character: ",
            "terrain": "Enter a type of terrain: ",
            "weather_condition": "Enter a weather condition: ",
            "place2": "Enter another place: ",
            "emotion2": "Enter another emotion: ",
            "adverb": "Enter an adverb: "
        }
    },

    "2": {
        "name": "Marathi",
        "file": "story1.txt",
        "prompts": {
            "adjective": "विशेषण लिहा: ",
            "place": "ठिकाणाचे नाव लिहा: ",
            "animal": "प्राण्याचे नाव लिहा: ",
            "emotion": "भावना लिहा: ",
            "object": "वस्तूचे नाव लिहा: ",
            "character": "पात्राचे नाव लिहा: ",
            "terrain": "भूप्रदेशाचे नाव लिहा: ",
            "weather_condition": "हवामानाची स्थिती लिहा: ",
            "place2": "दुसऱ्या ठिकाणाचे नाव लिहा: ",
            "emotion2": "दुसरी भावना लिहा: ",
            "adverb": "क्रियाविशेषण लिहा: "
        }
    },

    "3": {
        "name": "Hindi",
        "file": "story2.txt",
        "prompts": {
            "adjective": "एक विशेषण लिखें: ",
            "place": "एक जगह का नाम लिखें: ",
            "animal": "एक जानवर का नाम लिखें: ",
            "emotion": "एक भावना लिखें: ",
            "object": "एक वस्तु का नाम लिखें: ",
            "character": "एक पात्र का नाम लिखें: ",
            "terrain": "एक भूभाग का नाम लिखें: ",
            "weather_condition": "मौसम की स्थिति लिखें: ",
            "place2": "दूसरी जगह का नाम लिखें: ",
            "emotion2": "दूसरी भावना लिखें: ",
            "adverb": "एक क्रिया-विशेषण लिखें: "
        }
    }
}


def madlibs():

    print("\n================================")
    print("       MAD LIBS GENERATOR")
    print("================================")

    print("\nChoose your language:")
    print("1. English")
    print("2. Marathi (मराठी)")
    print("3. Hindi (हिंदी)")

    choice = input("\nEnter your choice (1/2/3): ").strip()

    if choice not in languages:
        print("Invalid language choice!")
        return

    selected_language = languages[choice]

    print("\nYou selected:", selected_language["name"])
    print("\nEnter the following words to create your story!\n")

    # Read the selected story file
    story_path = BASE_DIR / selected_language["file"]

    with open(story_path, "r", encoding="utf-8") as f:
        story = f.read()

    # Find all placeholders in the story
    words = list(dict.fromkeys(re.findall(r"<(.*?)>", story)))

    answers = {}

    # Take input for each placeholder
    for word in words:

        prompt = selected_language["prompts"].get(
            word, f"Enter {word}: "
        )

        answer = input(prompt).strip()

        answers[word] = answer

    # Replace placeholders with user answers
    for word, answer in answers.items():
        story = story.replace(f"<{word}>", answer)

    # Display the completed story
    print("\n================================")
    print("          YOUR STORY")
    print("================================\n")

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
