from turtle import Turtle

# Constants for text alignment and font styling
ALIGNMENT = "center"
FONT = ("Courier New", 24, "normal")

class Scoreboard(Turtle):
    """
    Manages the score display for the Snake Game.
    Inherits from the Turtle class to utilize built-in drawing functionality.
    """

    def __init__(self):
        """Initializes the scoreboard, sets the starting score, and displays it."""
        super().__init__()
        self.score = 0  # Starting score
        self.color("white")  # Score text color
        self.penup()  # Prevent drawing lines when moving
        self.goto(0, 270)  # Position scoreboard at the top of the screen
        self.hideturtle()  # Hide the turtle icon
        self.update_scoreboard()  # Display initial score

    def update_scoreboard(self):
        """Updates the scoreboard display with the current score."""
        self.clear()  # Clears the previous score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)  # Draws the updated score

    def increase_score(self):
        """Increases the score by 1 and refreshes the scoreboard."""
        self.score += 1  # Increment score
        self.update_scoreboard()  # Refresh display to show new score
