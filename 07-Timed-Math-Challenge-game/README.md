
# 🧮 Project 07: Timed Math Challenge

A command-line based **Timed Math Challenge** built using Python.

This project generates random mathematical questions using addition, subtraction, multiplication, and division. Users must solve 10 questions as quickly as possible while the program tracks their correct answers, wrong attempts, and total completion time.

## 🎯 Project Objectives

- Practise Python programming through a real-world mini project.
- Improve mathematical calculation skills.
- Understand Python functions and loops.
- Learn random number generation.
- Work with time measurement in Python.
- Practise exception handling and input validation.

## ✨ Features

- Generates random mathematical questions.
- Supports four mathematical operators:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (*)
  - Division (/)
- Generates 10 questions per challenge.
- Division questions have whole-number answers.
- Allows users to retry incorrect answers.
- Validates numerical input.
- Counts correct answers and wrong attempts.
- Measures total challenge completion time.
- Calculates accuracy percentage.
- Displays average time per question.
- Shows a final performance report.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Modules:**
  - `random` – Generates random mathematical questions.
  - `time` – Measures the total time taken to complete the challenge.

## 📂 Project Structure

```text
07-timed-math-challenge/
│
├── math_quiz.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ankitakatkar2024/21-Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd 21-Python-Projects/07-timed-math-challenge
```

### 3. Run the Python Program

```bash
python math_quiz.py
```

## 💻 Sample Output

```text
========================================
        TIMED MATH CHALLENGE
========================================

Solve 10 mathematical questions.
Operators: +, -, *, /
Division questions have whole-number answers.
Try to complete the challenge as quickly as possible.

Press Enter to start the challenge...

----------------------------------------

Problem #1: 11 + 9 = 20
Correct!

Problem #2: 8 - 12 = -4
Correct!

Problem #3: 7 * 4 = 28
Correct!

Problem #4: 48 / 4 = 12
Correct!

----------------------------------------

           FINAL RESULTS
----------------------------------------
Total Questions : 10
Correct Answers : 8
Wrong Attempts  : 3
Accuracy        : 80.00%
Total Time      : 2 min 45.69 sec
Average Time    : 16.57 seconds
----------------------------------------
Good performance!
```

*Note: Sample output is illustrative. Actual questions and results will vary.*

## 📚 Python Concepts Learned

| Concept | Application |
|---|---|
| Variables | Store scores and configuration values |
| Data Types | Work with integers, floats and strings |
| Lists | Store mathematical operators |
| Random Module | Generate random questions |
| Functions | Organise the program into reusable blocks |
| Conditional Statements | Calculate answers and check results |
| For Loop | Generate 10 questions |
| While Loop | Allow retries for incorrect answers |
| Try-Except | Handle invalid user input |
| Time Module | Measure challenge duration |
| String Formatting | Display questions and results |
| Arithmetic Operators | Perform mathematical calculations |

## 🚀 Future Improvements

- Add Easy, Medium and Hard difficulty levels.
- Add a leaderboard to save high scores.
- Allow users to choose the number of questions.
- Add a countdown timer for each question.
- Save previous challenge results in a file.
- Add a graphical user interface (GUI).

## 👩‍💻 Author

**Ankita Katkar**

B.Sc. Computer Science

GitHub: [@ankitakatkar2024](https://github.com/ankitakatkar2024)

---

⭐ This project is part of my **21 Python Projects Challenge**, where I build Python projects to improve my programming skills, logical thinking, and practical development experience.
