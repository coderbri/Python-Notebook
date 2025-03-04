# The Turtle Crossing Game [Capstone Project] – Update Log

<!-- TODO:
## Project Overview 

- to be filled out later

## gameplay mechanics

1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.

-->


## Update 1: Main Game Setup
**Date:** 20250304

**Objective:** Set up the basic game structure, including the screen, player, and car manager, and implement the game loop.

### Steps Taken:
1. **Initialized the game window**
    - Set up a 600x600 px screen with `screen.bgcolor("AntiqueWhite")`.
    - Disabled automatic screen updates using `screen.tracer(0)` to manually control rendering.

2. **Created the `Player` class**
    - Defined a `Player` class in `player.py` using Turtle graphics.
    - The turtle starts at the bottom of the screen and can only move forward when pressing "W."

3. **Created the `CarManager` class**
    - Defined a basic `CarManager` class in `car_manager.py`.
    - Set up a single car as a placeholder, facing left.

4. **Set up the game loop**
    - Added a `while game_is_on` loop to continuously update the screen.
    - Used `time.sleep(0.1)` to control game speed.

### Code Highlights:

#### `main.py`
```python
import time
from turtle import Screen

from player import Player
from car_manager import CarManager

# * 0. Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("AntiqueWhite")
screen.title("Turtle Crossing")
screen.tracer(0)

test_player = Player()
test_car = CarManager()

screen.listen()
screen.onkeypress(test_player.move_forwards, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
```

#### `player.py`

```py
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green", "#9FFFB0")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
```

#### `car_manager.py`

```py
from turtle import Turtle

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.setheading(270)    # to face east
        self.penup()
```

<!-- TODO:
---

## Update 2: Create the Player Behavior

- add date
- add objective
- add steps made in the project
- add code highlights

-->

---

## Upcoming Features:

- [x] 1. Main Game Setup

- [ ] 2. Create the Player Behavior
<!-- Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. -->

- [ ] 3. Create the Car Behavior
<!-- Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. -->

- [ ] 4. Detect when the Turtle Collides with a Car (Game Over Logic)
<!-- Detect when the turtle player collides with a car and stop the game if this happens. -->

- [ ] 5. Detect when the Player has reached the other side
<!-- Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. -->

- [ ] 6. Add the Scoreboard and Game Over Sequence
<!-- Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. -->

---

## Acknowledgments

Inspired by the mobile game, Crossy Road, and built as part of a Python learning journey through Dr. Angela Yu’s **100 Days of Code: Python Pro Bootcamp.**

---
<section align="center">
  <code>coderBri © 2025</code>
</section>