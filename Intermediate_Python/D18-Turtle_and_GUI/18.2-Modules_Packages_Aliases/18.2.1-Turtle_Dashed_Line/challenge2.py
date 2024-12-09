from turtle import Turtle, Screen

tim = Turtle()

tim.shape("turtle")
tim.color("teal", "#AFEEEE")

# Draw a dotted line
for _ in range(15):
    tim.forward(10)      # move forwards 10 steps (visibly)
    tim.penup()          # ? No ink will be drawn
    tim.forward(10)      # move forwards 10 steps (invisibly)
    tim.pendown()        # ? Ink will be drawn


screen = Screen()
screen.exitonclick()
