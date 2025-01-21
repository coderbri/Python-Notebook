import time
from turtle import Screen, Turtle

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)            # ? stops constant refresh

snake = Snake()

# 3. Control the Snake
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()         # ? refreshes screen btwn snake movements
    time.sleep(0.1)         # ? adds delay btwn movements before screen refresh

    snake.move()


# 4. Detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall

screen.exitonclick()
