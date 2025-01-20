from turtle import Screen, Turtle

# 0. Setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


# 1. Create the Snake
# ? create a tuple housing the location of the snake's initial body
starting_positions = ((0, 0), (-20, 0), (-40, 0))

# ? create the snake through a loop via segments
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)


# 2. Move the Snake
# 3. Control the Snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall

screen.exitonclick()
