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

#         east -> north -> west -> south
directions = [0, 90, 180, 270]

# ? Makes the drawn lines thicker
timmy.pensize(10)
timmy.speed("fast")

# * Generate a Random Walk
for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    """? `.setheading()` set's turtle's orientation to direction's angle."""


screen = Screen()
screen.exitonclick()
