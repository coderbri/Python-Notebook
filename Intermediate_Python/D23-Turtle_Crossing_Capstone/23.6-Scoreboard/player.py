from turtle import Turtle

# Constants for the player's behavior
STARTING_POSITION = (0, -280)   # ? The initial position of the turtle
MOVE_DISTANCE = 10              # ? The number of pixels the turtle moves forward
FINISH_LINE_Y = 280             # ? The Y-coordinate the turtle needs to reach to win

# * 2. Create the Player Behavior
class Player(Turtle):
    """A class representing the player-controlled turtle in the game."""

    def __init__(self):
        """Initialize the player's turtle at the starting position."""
        super().__init__()
        self.shape("turtle")
        self.color("green", "#9FFFB0")
        self.penup()
        self.got_to_start()
        self.setheading(90)

    def move_forwards(self):
        """Move the turtle forward (north) by MOVE_DISTANCE pixels."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def got_to_start(self):
        """Reset the turtle's position to the starting point."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the turtle has crossed the finish line."""
        return self.ycor() > FINISH_LINE_Y
