from turtle import Turtle

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(270)    # to face east
        self.penup()
