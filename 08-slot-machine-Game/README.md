# 🎰 Project 08: Slot Machine

A command-line based **Slot Machine Game** built using Python.

This project simulates a simple casino-style slot machine where players deposit virtual money, place bets, spin the reels, and try their luck at matching symbols to win rewards.

## 🎯 Project Objectives

- Practise Python programming through an interactive game.
- Understand random number generation.
- Improve logical thinking and problem-solving skills.
- Learn functions, loops, and conditional statements.
- Practise user input validation and balance management.

## ✨ Features

- Deposit virtual money into the game.
- Place bets on each spin.
- Generate random slot machine symbols.
- Display three spinning reels.
- Check matching symbols to determine winnings.
- Calculate rewards based on symbol combinations.
- Update the player's balance after every spin.
- Prevent bets that exceed the available balance.
- Continue playing until the user decides to quit or runs out of money.

## 🎮 How to Play

1. Start the game.
2. Enter the amount of virtual money you want to deposit.
3. Choose how much money to bet.
4. Spin the slot machine.
5. Match the symbols to win.
6. Your balance will be updated based on the result.
7. Continue playing or quit the game.

## 🏆 Game Rules

- The player must have a positive balance to play.
- Each spin requires a valid bet.
- The bet cannot exceed the available balance.
- Matching symbols determine the winning combination.
- Winnings are added to the player's balance.
- The game ends when the player quits or has insufficient money to continue.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Modules:**
  - `random` – Generates random slot machine symbols.

## 📂 Project Structure

```text
08-slot-machine/
│
├── slot_machine.py
└── README.md
```

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/ankitakatkar2024/21-Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd 21-Python-Projects/08-slot-machine
```

### 3. Run the Python Program

```bash
python slot_machine.py
```

## 💻 Sample Output

```text
========================================
          WELCOME TO SLOT MACHINE
========================================

Enter your deposit amount: 100

Your current balance: ₹100

Enter your bet amount: 10

Spinning...

🍒 | 🍒 | 🍒

Congratulations! You won!

Your winning amount: ₹50

Current balance: ₹140

Would you like to play again? (y/n): y
```

*Note: This is illustrative sample output. Actual symbols and winnings depend on the game's implementation.*

## 📚 Python Concepts Learned

| Concept | Application |
|---|---|
| Variables | Store balance, bets and winnings |
| Data Types | Work with integers, strings and lists |
| Lists | Store available slot machine symbols |
| Random Module | Generate random symbols |
| Functions | Organise game logic |
| Conditional Statements | Check winning combinations |
| While Loops | Allow repeated gameplay |
| For Loops | Generate and display reels |
| User Input | Accept deposits and bets |
| Exception Handling | Handle invalid input |
| Arithmetic Operations | Calculate bets and rewards |

## 🚀 Future Improvements

- Add different difficulty levels.
- Introduce multiple winning combinations.
- Add betting multipliers.
- Save high scores and player statistics.
- Create a graphical user interface (GUI).
- Add sound effects and spinning animations.

## 👩‍💻 Author

**Ankita Katkar**

Computer Science Graduate | Python Learner | Developer

GitHub: [@ankitakatkar2024](https://github.com/ankitakatkar2024)

---

⭐ This project is part of my **21 Python Projects Challenge**, where I build Python projects to improve my programming skills, logical thinking, and practical development experience.