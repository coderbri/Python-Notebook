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

---

## Update 2: Create the Player Behavior
**Date:** 20250305

**Objective:** Implement the player’s movement so that a turtle starts at the bottom of the screen and moves forward when pressing the “Up” key.

### Steps Taken:

1. **Created the player character**
   - Defined a `Player` class in `player.py`, inheriting from `Turtle`.
   - The turtle is initialized at the bottom of the screen `(0, -280)`.

2. **Implemented movement mechanics**
   - The turtle moves forward by a fixed distance (`MOVE_DISTANCE = 10`) when pressing "W."
   - The turtle is restricted to only moving north.

3. **Integrated player input**
   - Used `screen.listen()` in `main.py` to detect key presses.
   - Bound the `"w"` key to `test_player.move_forwards()`.


### Code Highlights:

#### `main.py`

```python
from player import Player

# Create an instance of the Player class
test_player = Player()

# Listen for user input and bind the "W" key to the turtle’s movement
screen.listen()
screen.onkeypress(test_player.move_forwards, "w")
```

#### `player.py`

```python
from turtle import Turtle

# Constants for the player's behavior
STARTING_POSITION = (0, -280)   # ? The initial position of the turtle
MOVE_DISTANCE = 10              # ? The number of pixels the turtle moves forward
FINISH_LINE_Y = 280             # ? The Y-coordinate the turtle needs to reach to win

class Player(Turtle):
    """A class representing the player-controlled turtle in the game."""

    def __init__(self):
        """Initialize the player's turtle at the starting position."""
        super().__init__()
        self.shape("turtle")
        self.color("green", "#9FFFB0")  # ? Green turtle with a lighter green shell
        self.penup()
        self.setheading(90)             # ? Face the turtle upwards
        self.goto(STARTING_POSITION)

    def move_forwards(self):
        """Move the turtle forward (north) by MOVE_DISTANCE pixels."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)
```

---

## Update 3: Create the Car Behavior
**Date:** 20250306

**Objective:** Implement moving cars that spawn randomly along the y-axis and move leftward across the screen.
- Cars should be **20px high** by **40px wide**.
- They should **spawn randomly** but **avoid** the top and bottom **50px** of the screen (safe zones).
- A new car is generated only **every 6th loop cycle** to prevent overcrowding.

### Steps Taken:
1. **Created the `CarManager` class**
    - Stores and manages all moving cars in a list (`self.all_cars`).

2. **Implemented car spawning logic**
    - Randomly generates a car **only 1/6th of the time** per game loop.
    - Assigns a **random color** from predefined palettes.
    - Cars spawn **on the right edge** (`x=300`) at a **random y-coordinate** within safe bounds (`-225 to 225`).

3. **Implemented movement logic**
    - Cars move **leftward** (`car.backward()`) by the **starting move distance** (`STARTING_MOVE_DISTANCE = 5`).
    - This movement will later be **increased** to create difficulty progression.

### Code Highlights:

#### `main.py`

```python
import time
from turtle import Screen
from player import Player
from car_manager import CarManager

# Create player and car manager instances
player = Player()
car_manager = CarManager()

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # * 3. Create the Car Behavior
    car_manager.create_car()  # Randomly create cars
    car_manager.move_cars()   # Move all cars leftward

screen.exitonclick()
```

#### `car_manager.py`

```python
import random
from turtle import Turtle

# Constants for car behavior
COLORS = ["#FCC1C1", "#FCDFC1", "#FCFCC1", "#C1FCDF", "#C1E0FC", "#C1C2FC"]  # Car fill colors
COLORS_OUTLINE = ["red", "orange", "goldenrod", "green", "blue", "purple"]   # Car outline colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 10         # Speed increase per level

# * 3. Create the Car Behavior
class CarManager:

    def __init__(self):
        """Initialize the CarManager with an empty list of cars."""
        self.all_cars = []

    def create_car(self):
        """Randomly generates a car and adds it to the game.
        A new car is created only 1 out of every 6 game loops to prevent overcrowding.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Limits car creation frequency
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Resize to 20x40 px
            new_car.penup()
            new_car.color(random.choice(COLORS_OUTLINE), random.choice(COLORS))

            # Generate a random y-coordinate within safe bounds (-225 to 225)
            random_y = random.randint(-225, 225)
            new_car.goto(300, random_y)  # Cars start from the right edge

            self.all_cars.append(new_car)  # Add to car list

    def move_cars(self):
        """Moves all cars leftward across the screen."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)  # Move each car left by 5 pixels
```

---

## Update 4: Detect when the Turtle Collides with a Car (Game Over Logic)
**Date:** 20250306

**Objective:** Detect when the turtle player collides with a car and stop the game if this happens.

### **Steps Taken**
- Iterated through all cars in `car_manager.all_cars`.
- Checked if the turtle’s distance from any car is less than 20px.
- If a collision occurs, the game loop stops.

### Code Highlights

#### `main.py`
```py
game_is_on = True
while game_is_on:

    # * 4. Detect when the Turtle Collides with a Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False  # Stops the game loop on collision

screen.exitonclick()
```

---

## Update 5: Detect when the Player has reached the other side
**Date:** 20250307

**Objective:**  
- Detect when the turtle player reaches the top edge of the screen (FINISH_LINE_Y).  
- When the player reaches the finish line:
    - Reset the turtle to the starting position.  
    - Increase the speed of the cars using `MOVE_INCREMENT`.  

### **Steps Taken:**
- Implemented `is_at_finish_line()` in `Player` class to check if the turtle has reached the goal.  
- Created `got_to_start()` to reset the turtle’s position after reaching the finish line.  
- Added `level_up()` in `CarManager` to increase car speed after each successful crossing.  
- Integrated logic into `main.py` to trigger these behaviors when the turtle wins.  

### **Code Highlights**  

#### `main.py`
```py
player = Player()
car_manager = CarManager()

game_is_on = True
while game_is_on:

    # * 5. Detect when the Player has reached the other side
    if player.is_at_finish_line():
        player.got_to_start()   # ? Reset turtle position
        car_manager.level_up()  # ? Increase car speed
```

#### `player.py`

```py
from turtle import Turtle

# Constants for the player's behavior
STARTING_POSITION = (0, -280)   # ? The initial position of the turtle
MOVE_DISTANCE = 10              # ? The number of pixels the turtle moves forward
FINISH_LINE_Y = 280             # ? The Y-coordinate the turtle needs to reach to win

# * 2. Create the Player Behavior
class Player(Turtle):
    """A class representing the player-controlled turtle in the game."""

    def __init__(self):
        """Initialize the player's turtle at the starting position."""
        super().__init__()
        self.shape("turtle")
        self.color("green", "#9FFFB0")
        self.penup()
        self.got_to_start()
        self.setheading(90)

    def move_forwards(self):
        """Move the turtle forward (north) by MOVE_DISTANCE pixels."""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def got_to_start(self):
        """Reset the turtle's position to the starting point."""
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        """Check if the turtle has crossed the finish line."""
        return self.ycor() > FINISH_LINE_Y
```

#### `car_manager.py`

```py
import random
from turtle import Turtle

# Constants for car behavior
COLORS = ["#FCC1C1", "#FCDFC1", "#FCFCC1", "#C1FCDF", "#C1E0FC", "#C1C2FC"]
COLORS_OUTLINE = ["red", "orange", "goldenrod", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 5          # Speed increase per level

# * 3. Create the Car Behavior
class CarManager:

    def __init__(self):
        """Initialize the CarManager with an empty list of cars."""
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    # ...

    def move_cars(self):
        """Moves all cars leftward across the screen."""
        for car in self.all_cars:
            car.backward(self.car_speed)    # Move each car left by incremented pixels

    # * 5. Detect when the Player has reached the other side
    def level_up(self):
        """Increase the speed of cars when the player reaches the finish line."""
        self.car_speed += MOVE_INCREMENT    # Gradually increase speed per level
```

---

## Update 6: Add the Scoreboard and Game Over Sequence
**Date:** 20250310

**Objective:**
- Create a scoreboard to track the player's level.
- Increase the level each time the player successfully crosses the road.
- Display "GAME OVER" in the center of the screen when the turtle collides with a car.

### **Steps Taken:**
- Implemented the `Scoreboard` class to manage level tracking and display updates.
- Added `update_scoreboard()` to refresh the displayed level.
- Created `increase_level()` to increment the level upon successful crossings.
- Implemented `game_over()` to display a "GAME OVER" message when the player loses.
- Integrated the scoreboard into `main.py`, ensuring updates occur upon level advancement and game-ending collisions.

### **Code Highlights**

#### `main.py`
```py
from scoreboard import Scoreboard

# Create Object instances
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:

    # * 4. Detect when the Turtle Collides with a Car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            # * Display Game Over Message
            scoreboard.game_over()

    # * 5. Detect when the Player has reached the other side
    if player.is_at_finish_line():
        player.got_to_start()
        car_manager.level_up()
        # * Increase Scoreboard Level
        scoreboard.increase_level()
```

#### `scoreboard.py`
```py
from turtle import Turtle
# Font configuration for scoreboard display
FONT = ("Courier", 24, "normal")

# * 6. Add the Scoreboard and Game Over Sequence
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("#000")
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Refresh the displayed level on the screen."""
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """Increment the level count and update the scoreboard."""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Display the 'GAME OVER' message at the center of the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

```

---

## Acknowledgments

Inspired by the mobile game, Crossy Road, and built as part of a Python learning journey through Dr. Angela Yu’s **100 Days of Code: Python Pro Bootcamp.**

---
<section align="center">
  <code>coderBri © 2025</code>
</section>