import time
from turtle import Screen

from player import Player
from car_manager import CarManager

# * 1. Main Game Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AntiqueWhite")
screen.title("Turtle Crossing")
screen.tracer(0)

# Create player and car manager instances
player = Player()
car_manager = CarManager()

# * 2. Create the Player Behavior
screen.listen()
screen.onkeypress(player.move_forwards, "w")

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # * 3. Create the Car Behavior
    car_manager.create_car()
    car_manager.move_cars()

    # * 4. Detect when the Turtle Collides with a Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    # * 5. Detect when the Player has reached the other side
    if player.is_at_finish_line():
        player.got_to_start()       # ? Reset turtle position
        car_manager.level_up()      # ? Increase car speed

screen.exitonclick()
