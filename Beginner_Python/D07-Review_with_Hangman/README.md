# Putting Everything into Practice by Building Hangman

This project applies essential Python concepts, such as `if`/`else` statements, `for` loops, lists, string manipulation, and module importing, by building an interactive Hangman game. 

## Step 1 - Picking a Random Word and Checking Answers

- The `random` module is used to randomly select a word from a predefined list of words imported from `hangman_words.py`.
- User input is handled with `input()`, and the guessed letter is converted to lowercase for consistency.
- A loop is implemented to check if the guessed letter matches any letter in the chosen word, printing "Right" or "Wrong" accordingly.

## Step 2 - Replacing Blanks with Guesses

- The game sets up a `placeholder` string filled with underscores (`_`) to represent each letter in the word to be guessed.
- The `display` string updates based on the user's guesses, revealing correctly guessed letters in their respective positions and leaving underscores for letters that are yet to be guessed. For instance, guessing "p" in "apple" updates `display` to `_ p p _ _`.
- This allows the game to give real-time feedback on each guess by showing which letters have been correctly guessed.

## Step 3 - Checking if the Player has Won

- A `while` loop allows the player to continue guessing until the chosen word is fully revealed or the player runs out of lives.
- The game checks if `display` has any remaining blanks (`_`). If no blanks are left, it declares a win.
- The loop updates `display` to retain previously guessed letters, ensuring that each correct guess is saved and shown throughout the game.

## Step 4 - Keeping Track of the Player’s Lives

- A `lives` variable, initially set to 6, tracks the player’s remaining attempts.
- If the player guesses a letter that is not in the word, `lives` decreases by 1, and the player is notified of the incorrect guess and the remaining lives.
- The game ends when `lives` reaches 0, at which point the player loses, and the correct word is revealed.
- The game uses ASCII art from `hangman_art.py` to visually display the player’s progress and remaining attempts.

## Step 5 - Improving the User Experience

- The word list and ASCII art are managed in external files (`hangman_words.py` and `hangman_art.py`), which the main game imports for cleaner code organization.
- The logo from `hangman_art.py` is displayed at the start to enhance the game’s presentation, creating a more immersive user experience.
