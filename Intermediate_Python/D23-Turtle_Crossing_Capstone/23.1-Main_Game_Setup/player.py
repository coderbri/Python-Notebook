from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green", "#9FFFB0")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
