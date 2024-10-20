

https://github.com/user-attachments/assets/35723a72-ae66-462e-a93d-f0318c754a6b

![mastermind](https://github.com/user-attachments/assets/9b3a094f-d7da-4280-9aa8-7809972e6df2)
# Mastermind Color Guessing Game
# Description
This project is a Pygame-based implementation of the popular Mastermind game. The objective of the game is to guess a secret color code within a limited number of tries. Players will select colors from a set of options and receive feedback on the correctness of their guesses.

# Features
1. Interactive Color Selection: Players can choose colors using on-screen buttons.
2. Feedback System: After each guess, feedback is provided on how many colors are correct and in the right position or incorrect positions.
3. 10 Attempts: Players have up to 10 attempts to guess the secret color combination.
4. Reset Button: Allows the player to reset the game at any time with a new randomly generated code.

# Gameplay
1. The secret code is randomly generated from the available colors: Red, Green, Blue, Yellow, White, and Orange.
2. The player selects four colors per guess by clicking on the color buttons on the right of the game board.
3. Once four colors are selected, the player presses Enter to submit the guess.
4. Feedback is shown after each guess indicating how many colors are correct and in the correct or incorrect positions.
5. The player wins if they guess the code correctly within 10 tries.
6. If all attempts are exhausted without guessing correctly, the player loses, and the correct code is revealed.

# Requirements
1. Python 3.x
2. Pygame

# Installation
1. Clone this repository or download the files manually: git clone https://github.com/Hamadabcn/mastermind_game.git
2. Install the required Pygame package: pip install pygame
3. Run the game: python main.py

# How to Play
1. Launch the game by running the main.py file.
2. Use the color buttons on the right to select your guess.
3. Once you've selected 4 colors, press Enter to submit your guess.
4. Try to guess the secret code in 10 tries or less.
5. If you guess correctly, a Congratulations message will appear.
6. If you fail to guess the code in 10 tries, the correct code will be displayed, and you'll lose the game.
7. Press the Reset Game button to restart the game with a new code.

# Game Controls
1. Mouse Click: Select a color by clicking on the buttons.
2. Enter Key: Submit your current guess.
3. Reset Button: Restart the game.

# Contributing
Feel free to fork this project, make improvements, or report issues. Pull requests are welcome!

# License
This project is licensed under the MIT License.
