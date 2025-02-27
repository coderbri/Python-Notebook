from turtle import Turtle

# * 4. Create a Ball and Make it Move
class Ball(Turtle):

    def __init__(self):
        """Initializes the ball at the center of the screen with default properties."""
        super().__init__()
        self.color("#fff")
        self.shape("circle")
        self.penup()
        # ? since it's default size is 20 x 20, we don't need the below method
        # self.shapesize(stretch_wid=1, stretch_len=1)

    def move(self):
        """Moves the ball diagonally by updating its x and y coordinates."""
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
