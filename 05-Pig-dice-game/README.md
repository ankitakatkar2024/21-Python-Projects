
# 🎲 Pig Dice Game

A multiplayer command-line Pig Dice Game built using Python.

Players take turns rolling a six-sided dice to earn points. They can choose to keep rolling or save their current turn points. However, rolling a 1 means losing all points earned during that turn.

The first player to reach 50 points wins the game!

---

## 🚀 Features

- Supports 2 to 4 players.
- Random dice rolling using Python's random module.
- Players can roll or hold their points.
- Rolling a 1 resets the current turn score to zero.
- Individual player score tracking.
- Automatic winner detection.
- Input validation for player count and choices.
- Replay option to start a new game.
- Simple and interactive command-line interface.

---

## 🛠️ Technologies Used

- Python 3
- Random Module
- Functions
- While Loops
- For Loops
- Conditional Statements
- Lists
- User Input Handling

---

## 📂 Project Structure

```text
pig-dice-game/
│
├── pig_dice_game.py
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd pig-dice-game
```

### 3. Run the game

```bash
python pig_dice_game.py
```

No external libraries are required.

---

## 🎮 How to Play

1. Enter the number of players (2–4).
2. Each player takes turns rolling the dice.
3. Enter `y` to roll the dice.
4. Enter `n` to stop and save the current turn points.
5. If you roll a 1, you lose all points earned during that turn.
6. The first player to reach 50 points wins.
7. Choose whether to play again.

---

## 📸 Sample Output

```text
Enter the number of players (2-4): 2

========================================
Player 1's turn
Total score: 0
========================================

Roll the dice? (y/n): y
You rolled: 6
Current turn score: 6

Roll the dice? (y/n): y
You rolled: 4
Current turn score: 10

Roll the dice? (y/n): n

Turn ended!
Player 1 total score: 10
```

---

## 📚 Concepts Learned

- Generating random numbers.
- Creating and calling functions.
- Using loops for repeated gameplay.
- Managing multiple players with lists.
- Implementing game logic.
- Validating user input.
- Tracking scores and identifying winners.

---

## 🔮 Future Improvements

- Add a graphical user interface using Pygame.
- Add a scoreboard and player names.
- Add different winning score options.
- Add dice rolling animations.
- Save game scores to a file.

---

## 👩‍💻 Author

**Ankita Katkar**

Computer Science Graduate | Python Learner

GitHub: [@ankitakatkar2024](https://github.com/ankitakatkar2024)

---

⭐ Built as part of my **21 Python Projects Challenge**.
