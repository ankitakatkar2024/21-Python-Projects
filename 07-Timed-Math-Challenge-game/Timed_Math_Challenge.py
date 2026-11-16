
# import random
# import time

# OPERATORS = ["+", "-", "*", "/"]
# MIN_OPERAND = 3
# MAX_OPERAND = 12
# TOTAL_PROBLEMS = 10


# def generate_problem():
#     left = random.randint(MIN_OPERAND, MAX_OPERAND)
#     right = random.randint(MIN_OPERAND, MAX_OPERAND)
#     operator = random.choice(OPERATORS)

#     expr = str(left) + " " + operator + " " + str(right)
#     answer = eval(expr)

#     return expr, answer

# wrong = 0
# input("Press Enter to start the timed math challenge...")
# print("---------------------------------")

# start_time = time.time()


# for i in range(TOTAL_PROBLEMS):
#     expr, answer = generate_problem()

#     while True:
#         guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")

#         try:
#             if float(guess) == answer:
#                 break
            
#             else:
#                 wrong += 1
#                 print("Incorrect! Try again.")

#         except ValueError:
#             print("Please enter a valid number.")
            
# end_time = time.time()
# total_time = end_time - start_time
            
# print("---------------------------------")
# print("\nYou completed the challenge with " + str(wrong) + " wrong answers.")
# print("Total time taken: " + str(round(total_time, 2)) + " seconds.")

#  Upgraded Timed Math Challenge 
import random
import time

# ==========================================
# PROJECT 07: TIMED MATH CHALLENGE
# ==========================================

OPERATORS = ["+", "-", "*", "/"]

MIN_OPERAND = 3
MAX_OPERAND = 12

TOTAL_PROBLEMS = 10


def generate_problem():
    """Generate a random mathematical problem."""

    operator = random.choice(OPERATORS)

    right = random.randint(MIN_OPERAND, MAX_OPERAND)

    if operator == "/":
        answer = random.randint(MIN_OPERAND, MAX_OPERAND)
        left = right * answer

    else:
        left = random.randint(MIN_OPERAND, MAX_OPERAND)

        if operator == "+":
            answer = left + right

        elif operator == "-":
            answer = left - right

        else:
            answer = left * right

    expression = f"{left} {operator} {right}"

    return expression, answer


def get_answer(expression):
    """Get a valid numerical answer from the user."""

    while True:
        guess = input(f"{expression} = ").strip()

        try:
            return float(guess)

        except ValueError:
            print("Invalid input! Please enter a number.")


def format_time(seconds):
    """Convert seconds into minutes and seconds."""

    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60

    return f"{minutes} min {remaining_seconds:.2f} sec"


def display_results(correct, wrong, total_time):
    """Display the final challenge results."""

    accuracy = (correct / TOTAL_PROBLEMS) * 100
    average_time = total_time / TOTAL_PROBLEMS

    print("\n" + "-" * 40)
    print("           FINAL RESULTS")
    print("-" * 40)

    print(f"Total Questions : {TOTAL_PROBLEMS}")
    print(f"Correct Answers : {correct}")
    print(f"Wrong Attempts  : {wrong}")
    print(f"Accuracy        : {accuracy:.2f}%")
    print(f"Total Time      : {format_time(total_time)}")
    print(f"Average Time    : {average_time:.2f} seconds")

    print("-" * 40)

    if accuracy == 100:
        print("Excellent! Perfect score!")

    elif accuracy >= 70:
        print("Good performance!")

    elif accuracy >= 40:
        print("Keep practising!")

    else:
        print("You need more practice!")


def math_challenge():

    print("\n" + "=" * 40)
    print("        TIMED MATH CHALLENGE")
    print("=" * 40)

    print(f"\nSolve {TOTAL_PROBLEMS} mathematical questions.")
    print("Operators: +, -, *, /")
    print("Division questions have whole-number answers.")
    print("Try to complete the challenge as quickly as possible.")

    input("\nPress Enter to start the challenge...")

    correct = 0
    wrong = 0

    print("\n" + "-" * 40)

    # Start timer
    start_time = time.perf_counter()

    for i in range(TOTAL_PROBLEMS):

        expression, answer = generate_problem()

        while True:

            print(f"\nProblem #{i + 1}: ", end="")

            guess = get_answer(expression)

            if guess == answer:
                print("Correct!")
                correct += 1
                break

            else:
                print("Incorrect! Try again.")
                wrong += 1

    # Stop timer
    end_time = time.perf_counter()

    total_time = end_time - start_time

    display_results(correct, wrong, total_time)


# Main program
if __name__ == "__main__":
    math_challenge()

