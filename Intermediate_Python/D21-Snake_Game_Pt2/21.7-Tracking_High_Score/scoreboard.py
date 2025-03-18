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
    - Tracking and persisting the high score using a .txt file
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        # ? Read high score from a file; default to 0 if file doesn't exist
        try:
            with open("data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)               # ? Position scoreboard at the top of the screen
        self.hideturtle()               # ? Hide the turtle icon
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and updates the display with the current score and high score."""
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the current score and updates the high score if a new record is reached."""
        if self.score > self.high_score:
            self.high_score = self.score
            # ? Save new high score to a file
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increases the score by 1 and refreshes the scoreboard display."""
        self.score += 1
        self.update_scoreboard()
