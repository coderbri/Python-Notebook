# Putting Everything into Practice by Building Hangman

At this point, significant progress has been made in Python fundamentals by applying key concepts such as `if`/`else` statements, `for` loops, and string manipulation. The Hangman game development has been initiated, with key tasks implemented. 

## Step 1 - Picking a Random Word and Checking Answers

- The `random` module is used to randomly select a word from a predefined list, demonstrating how to work with external libraries and lists.
- Input handling is practiced, where user guesses are converted to lowercase, emphasizing string manipulation techniques.
- A loop structure is employed to check whether the guessed letter matches any letters in the chosen word, outputting "Right" or "Wrong" for each character comparison. 


## Step 2 - Replacing Blanks with Guesses

TODO-1
- Create an empty String called placeholder.
- For each letter in the chosen_word, add a _ to placeholder. So if the chosen_word was "apple", placeholder should be _ _ _ _ _ with 5 "_" representing each letter to guess.

TODO-2
- Create an empty string called "display".
- Loop through each letter in the chosen_word.
- If the letter at that position matches guess then reveal that letter in the display at that position. e.g. If the user guessed "p" and the chosen word was "apple", then display should be _ p p _ _.
- Print display and you should see the guessed letter in the correct position.
- But every letter that is not a match is represented with a "_".


## Step 3 - Checking if the Player has Won

TODO-1
- Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word.
- At that point display has no more blanks ("_"). Then you can tell the user they've won.

TODO-2
- Update the for loop so that previous guesses are added to the display String.
- At the moment, when the user makes a new guess, the previous guess gets replaced by a "_". We need to fix that by updating the for loop.


## Step 4 - Keeping Track of the Player’s Lives

TODO-1:
- Create a variable called lives to keep track of the number of lives left.
- Set lives to equal 6.

TODO-2:
- If guess is not a letter in the chosen_word, Then reduce lives by 1.
- If lives goes down to 0 then the game should end, and it should print "You lose."

TODO-3:
- print the ASCII art from the list stages that corresponds to the current number of lives the user has remaining.

## Step 5 - Improving the User Experience

TODO-1:
- Update the word list to use the word_list from hangman_words.py

TODO-2:
- Update the code to use the stages from the file hangman_art.py

TODO-3:
- Import the logo from hangman_art.py and print it at the start of the game.
