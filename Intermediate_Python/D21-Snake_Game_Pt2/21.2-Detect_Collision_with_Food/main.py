import time
from turtle import Screen, Turtle

from food import Food
from snake import Snake

# Setup screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Stops automatic screen refresh, allowing manual updates

# Create game objects
snake = Snake()
food = Food()

# Control the Snake using arrow keys
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh screen after each movement
    time.sleep(0.1)  # Adds delay between movements for smoother gameplay
    snake.move()

    # 4. Detect collision with food
    if snake.head.distance(food) < 15:  # If snake's head is within 15 pixels of food
        print("nom nom nom")  # Temporary debug print for scorekeeping
        food.refresh()  # Moves food to a new random position

        # Future implementation: Extend the snake after eating food

# Future features:
# 5. Create a scoreboard
# 6. Detect collision with walls

screen.exitonclick()