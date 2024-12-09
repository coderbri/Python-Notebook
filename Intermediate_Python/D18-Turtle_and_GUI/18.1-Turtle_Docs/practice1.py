from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("teal", "#AFEEEE")

# Make the Turtle move straight then turn
timmy_the_turtle.forward(200)               # walks 200 steps east
timmy_the_turtle.right(90)                  # turn right by 90˚
timmy_the_turtle.forward(100)               # walks 100 steps south


screen = Screen()
screen.exitonclick()
