from turtle import Turtle

# Constants for the player's behavior
STARTING_POSITION = (0, -280)   # ? The initial position of the turtle
MOVE_DISTANCE = 10              # ? The number of pixels the turtle moves forward
FINISH_LINE_Y = 280             # ? The Y-coordinate the turtle needs to reach to win

# * 2. Create the Player Behavior
class Player(Turtle):
    
    def __init__(self):
        """Initialize the player's turtle at the starting position."""
        super().__init__()
        self.shape("turtle")
        self.color("green", "#9FFFB0")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        """Move the turtle forward (north) by MOVE_DISTANCE pixels."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
