from turtle import Turtle

STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake: # ? Creates a 3-segmented snake

    def __init__(self):
        self.segments = []      # ? create the snake through a loop via segments
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup() # ? fixes the weird thin line between segments when snake moves
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):  # ? move each snake segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # ? if clauses will prevent the snake backward movement
    def move_up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
