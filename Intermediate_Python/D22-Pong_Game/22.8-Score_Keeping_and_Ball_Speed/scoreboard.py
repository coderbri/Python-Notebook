from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 80, "normal")

# * 8. Score Keeping
class Scoreboard(Turtle):

    def __init__(self):
        """Initializes the scoreboard, tracks scores for both players, and displays the initial score."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        # ? Separate attributes for left and right player scores
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and updates the screen with the latest scores."""
        self.clear()
        self.goto(-100, 200)  # ? Left player's score position
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)  # ? Right player's score position
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increment_l_points(self):
        """Increments left player's score and updates the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def increment_r_points(self):
        """Increments right player's score and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
