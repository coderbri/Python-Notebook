from turtle import Turtle
# Font configuration for scoreboard display
FONT = ("Courier", 24, "normal")

# * 6. Add the Scoreboard and Game Over Sequence
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("#000")
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh the displayed level on the screen."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increment the level count and update the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display the 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
