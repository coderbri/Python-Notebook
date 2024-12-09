import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)    # ? set to RGB color mode

def generate_random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

#         east -> north -> west -> south
directions = [0, 90, 180, 270]

# ? Makes the drawn lines thicker
timmy.pensize(10)
timmy.speed("fastest")

# * Generate a Random Walk with Random Colors
for _ in range(200):
    timmy.color(generate_random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))
    """? `.setheading()` set's turtle's orientation to direction's angle."""


screen = t.Screen()
screen.exitonclick()
