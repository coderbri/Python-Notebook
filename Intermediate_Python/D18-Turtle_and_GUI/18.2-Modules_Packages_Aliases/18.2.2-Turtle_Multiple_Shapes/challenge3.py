import random
from turtle import Turtle, Screen

timmy = Turtle()

colors = ["dark slate gray",
        "teal",
        "dark cyan",
        "cadet blue",
        "light sea green",
        "medium turquoise",
        "dark turquoise",
        "pale turquoise",
        "light cyan",
        "powder blue",
        "light blue"
]

# Draw a Single Shape
def draw_shape(num_sides):
    for _ in range(num_sides):
        angle = 360 / num_sides       # ? sets the number of times, it will change angles (sides)
        timmy.forward(100)            # move forwards 100 steps
        timmy.right(angle)            # ? at the set angle, turn that degree to draw new side

# Draw Multiple Shapes
for shape_side_n in range(3, 11):     # ? from triangle (3, inclusive) to decagon (10, inclusive)
    timmy.color(random.choice(colors))
    draw_shape(shape_side_n)


screen = Screen()
screen.exitonclick()
