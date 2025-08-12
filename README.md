Number Guess Game :-

🎯A fun and simple number guessing game built with Python's Tkinter module. The player has 7 tries to guess a randomly generated number between 1 and 100, with hints after each guess.

📌 Features :-

Random number between 1 and 100 each game.

7 attempts to guess the correct number.

Hints: "Too low" or "Too high" with updated possible range.

Restart option to play again without closing the app.

User-friendly Tkinter GUI.

🖥️ Requirements :-

Python 3.x

Tkinter (comes pre-installed with Python)

▶️ How to Run :-

Save the code as number_guess_game.py.

Open a terminal or command prompt in the saved file's directory.

Run:

python number_guess_game.py

🎮 How to Play :-

The game will display "Guess a number between 1 and 100".

Type your guess into the input box and click Guess.

The game will tell you:

"Too low" → Guess higher.

"Too high" → Guess lower.

Keep guessing until you find the correct number or run out of tries.

Click Restart to start a new game.

📝 Code Highlights :-

Random number generation:

num = random.randint(1, 100)
Valid number checking to prevent crashes:

try:
    g = int(t1.get())
except ValueError:
    l2.config(text="Enter a valid number.")
Dynamic range hints for better guessing.
