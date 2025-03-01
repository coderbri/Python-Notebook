from turtle import Turtle

# * 2-3. Create Paddle Class and Move them via Key Presses
class Paddle(Turtle):

    def __init__(self, position):
        """Initialize paddle at the given position."""
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("#fff")
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves the paddle up by 20 pixels."""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves the paddle down by 20 pixels."""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
