import time
from turtle import Screen

from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard

# * 1. Main Game Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AntiqueWhite")
screen.title("Turtle Crossing")
screen.tracer(0)


# * 2. Create the Player Behavior
test_player = Player()
# test_car = CarManager()
# scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(test_player.move_forwards, "w")

game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
