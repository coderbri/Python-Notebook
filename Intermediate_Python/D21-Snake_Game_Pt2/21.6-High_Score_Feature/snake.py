from turtle import Turtle

# Constants for initial snake setup and movement
STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Represents the snake in the classic Snake game.
    Handles movement, growth, and direction control.
    """

    def __init__(self):
        """Initializes the snake with three starting segments."""
        self.segments = []              # ? List to store snake segments
        self.create_snake()
        self.head = self.segments[0]    # ? First segment as the snake's head

    def create_snake(self):
        """Creates the initial snake by adding segments at predefined positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Adds a new segment to the snake at the given position.
        Args: position (tuple): (x, y) coordinates for the new segment
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()             # ? Prevents drawing lines while moving
        new_segment.goto(position)
        self.segments.append(new_segment)

    # * 8. Reset Snake
    def reset(self):
        """Resets the snake by clearing all segments and recreating it from the start."""
        for seg in self.segments:
            seg.goto(1000, 1000)        # ? Move old segments off-screen
        self.segments.clear()           # ? Remove all segments from the list
        self.create_snake()             # ? Recreate the initial snake
        self.head = self.segments[0]    # ? Reset the head reference

    # 7. Extend & Detect Collision with Tail
    def extend(self):
        """
        Adds a new segment to the snake's tail.
        This is typically called when the snake eats food.
        """
        self.add_segment(self.segments[-1].position())  # Extends from the last segment's position

    def move(self):
        """Moves the snake forward by updating each segment's position."""
        for seg_num in range(len(self.segments) - 1, 0, -1):  # ? move each snake segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    """Movement methods:
    Each method changes the snake's direction unless it's currently moving in the opposite direction.
    """
    def move_up(self):
        """Changes direction to up unless moving down."""
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        """Changes direction to down unless moving up."""
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_left(self):
        """Changes direction to left unless moving right."""
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        """Changes direction to right unless moving left."""
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
