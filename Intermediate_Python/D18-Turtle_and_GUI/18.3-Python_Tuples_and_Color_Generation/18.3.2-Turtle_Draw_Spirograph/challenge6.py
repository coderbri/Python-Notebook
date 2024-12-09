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

timmy.speed("fastest")

# * Draw a Spirograph
def draw_spirograph(size_of_gap):
    """Accepts a single parameter, `gap_size`, which is the size between
    each drawn circle based on the arrow's direction heading."""
    for _ in range(int(360 / size_of_gap)):
        timmy.color(generate_random_color())
        timmy.circle(100)           # ? draws instant circle
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
