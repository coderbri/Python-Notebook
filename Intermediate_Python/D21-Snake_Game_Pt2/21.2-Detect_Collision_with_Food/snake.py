from turtle import Turtle

# Constants for snake movement
STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))  # Initial 3-segment snake
MOVE_DISTANCE = 20  # Distance moved per step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """Creates and controls a multi-segmented snake."""

    def __init__(self):
        self.segments = []  # Stores snake segments
        self.create_snake()
        self.head = self.segments[0]  # First segment is the snake's head

    def create_snake(self):
        """Creates the initial 3-segment snake."""
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()  # Prevents drawing lines between segments
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """Moves the snake forward by shifting segments."""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Moves segments forward
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)  # Moves the head forward

    # Direction controls (Prevents moving backward)
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)