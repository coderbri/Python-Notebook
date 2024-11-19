# Todo List

- [x] Import required modules: art, random and game data

- [x] Randomly select an account from the game data.
    - [x] Import random module and use random.choice() to choose a dictionary entry.
    - [x] Ensure that the second generated account is different from the first.

- [x] Format the account data into a printable format.

- [x] Ask user for guess and assign to choices 'A' or 'B'.

- [x] Check if user is correct.
    - [x] Get follower count of each account
    - [x] Use if statement to check if user is correct.
    - [x] Give user feedback on their guess. End game if user is right, otherwise continue game.
    - [x] Score Keeping.
    - [x] Make the game repeatable.
    - [x] Reassign account in position 'B' to position 'A'.
    - [x] Clear the screen and reprint logo.


#### Logic for TODO 5.2 `check_answer()` Function:

|           | Guess A | Guess B |
| :-------: | :-----: | :-----: |
| **A > B** | ✓ | X |
| **B > A** | X | ✓ |