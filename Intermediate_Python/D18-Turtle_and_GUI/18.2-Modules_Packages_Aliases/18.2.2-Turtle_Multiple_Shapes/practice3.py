from turtle import Turtle, Screen

tim = Turtle()

# Draw a Pentagon
num_sides = 5                   # Shape: pentagon
for _ in range(num_sides):
    angle = 360 / num_sides     # ? sets the number of times, it will change angles (sides)
    tim.forward(100)            # move forwards 100 steps
    tim.right(angle)            # ? at the set angle, turn that degree to draw new side


screen = Screen()
screen.exitonclick()
