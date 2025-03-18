from turtle import Turtle

# Constants for text alignment and font styling
ALIGNMENT = "center"
FONT = ("Courier New", 24, "normal")

class Scoreboard(Turtle):
    """
    Manages the score display for the Snake Game.
    Inherits from the Turtle class and handles:
    - Initializing and displaying the score
    - Updating the score when the player earns points
    - Displaying the 'Game Over' message
    """

    def __init__(self):
        super().__init__()
        self.score = 0              # Starting score
        self.high_score = 0         # Highest score
        self.color("white")         # Score text color
        self.penup()                # Prevent drawing lines when moving
        self.goto(0, 270)           # Position scoreboard at the top of the screen
        self.hideturtle()           # Hide the turtle icon
        self.update_scoreboard()    # Display initial score

    def update_scoreboard(self):
        """Clears the previous score and updates the display with the current score and high score."""
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # * 8. Retain Highest Score
    def reset(self):
        """Resets the current score and updates the high score if a new record is reached."""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score by 1 and refreshes the scoreboard display."""
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     """Displays the 'Game Over' message in the center of the screen."""
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #     print(f"GAME OVER. Final Score: {self.score}")
