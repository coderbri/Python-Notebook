from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet:", prompt="Which turtle will win the race? Enter a color: ")

outline_colors = ["red", "orange", "goldenrod", "green", "blue", "purple", "palevioletred"]
fill_colors = ["#FFB09F", "#FFE09F", "#EEFF9F", "#9FFFB0", "#9FEEFF", "#B09FFF", "#FF9FBE"]
y_positions = [-70, -40, -10, 20, 50, 80, 110]

for turtle_index in range(0, 7):
    tim = Turtle(shape="turtle")
    tim.color(outline_colors[turtle_index], fill_colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=-y_positions[turtle_index])


screen.exitonclick()
