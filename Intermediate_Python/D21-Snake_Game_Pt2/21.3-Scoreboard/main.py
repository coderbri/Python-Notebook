import time
from turtle import Screen

from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)            # ? stops constant refresh

snake = Snake()
food = Food()

# 5. Create a scoreboard
scoreboard = Scoreboard()

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
    if snake.head.distance(food) < 15:
        print("*nom nom nom*")
        scoreboard.increase_score()
        food.refresh()
        # logic needed to extend the tail with every food the snake eats


# 6. Detect collision with wall

screen.exitonclick()
