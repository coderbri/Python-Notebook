from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_clockwise():
    tim.right(10)
    '''Alternative Method:
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
    '''

def turn_counterclockwise():
    tim.left(10)
    '''Alternative Method:
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
    '''

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(turn_counterclockwise, "a")
screen.onkey(turn_clockwise, "d")
screen.onkey(clear_screen, "c")

screen.exitonclick()
