import time
from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    # ? stops constant refresh

starting_positions = ((0, 0), (-20, 0), (-40, 0))

# 2. Move the Snake
segments = []
# ? create the snake through a loop via segments
for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()     # ? fixes the weird thin line between segments when snake moves
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()         # ? update the screen between whole steps; simulates snake movement
    time.sleep(0.1)         # ? adds a 0.1 sec delay before segments move again

    # ? Range positions           start, stop, step
    for seg_num in range(len(segments) - 1, 0, -1): # ? move each snake segment
        new_x = segments[seg_num -1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


# 3. Control the Snake
# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall

screen.exitonclick()
