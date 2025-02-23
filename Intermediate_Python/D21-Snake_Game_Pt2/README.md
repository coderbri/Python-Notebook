# Snake Game: Update Log

## Project Overview
This repository documents the development of a Snake Game built using Python and the Turtle module. Each update corresponds to a significant milestone in the creation of the game, showcasing progressive implementation of features and functionality.

---

## Update 1: Setting Up the Screen and Creating the Snake
**Date:** 20250119

- **Objective:** Initialize the game screen and create the snake's starting segments.
- **Steps Completed:**
  1. Set up a black game screen with a 600x600 pixel dimension.
  2. Created three initial snake segments using Turtle objects positioned at specific coordinates.
- **Code Highlights:**
  ```python
  screen = Screen()
  screen.setup(width=600, height=600)
  screen.bgcolor("black")
  screen.title("My Snake Game")

  starting_positions = ((0, 0), (-20, 0), (-40, 0))
  for position in starting_positions:
      new_segment = Turtle("square")
      new_segment.color("white")
      new_segment.goto(position)
  ```

---

## Update 2: Moving the Snake
**Date:** 20250119

- **Objective:** Enable the snake to move continuously in the game space.
- **Steps Completed:**
  1. Implemented a list to store the snake segments for movement tracking.
  2. Configured a game loop using `while` to update the screen and move the snake.
  3. Added functionality for each segment to follow the one in front, simulating snake movement.
  4. Introduced a slight delay between screen updates to create a smooth movement effect.
- **Code Highlights:**
  ```python
  screen.tracer(0)            # Stops constant screen refresh
  segments = []
  for position in starting_positions:
      new_segment = Turtle("square")
      new_segment.color("white")
      new_segment.penup()     # Removes lines between segments
      new_segment.goto(position)
      segments.append(new_segment)

  game_is_on = True
  while game_is_on:
      screen.update()         # Refresh screen only once per loop
      time.sleep(0.1)         # Pause to control snake speed

      for seg_num in range(len(segments) - 1, 0, -1):
          new_x = segments[seg_num - 1].xcor()
          new_y = segments[seg_num - 1].ycor()
          segments[seg_num].goto(new_x, new_y)
      segments[0].forward(20)
  ```

---

## Update 2.5: Modularization with the Snake Class
**Date:** 20250119

- **Objective:** Refactor the snake logic into a standalone `Snake` class for modularity and reusability.
- **Steps Completed:**
  1. Created a `Snake` class in a separate `snake.py` file.
  2. Moved the snake creation and movement logic into methods of the `Snake` class.
  3. Updated the main game file to use the `Snake` class, simplifying the game loop.
- **Code Highlights:**
  - **`snake.py`**
    ```python
    from turtle import Turtle
    STARTING_POSITIONS = ((0, 0), (-20, 0), (-40, 0))
    MOVE_DISTANCE = 20

    class Snake:

        def __init__(self):
            self.segments = []      # Create the snake through a loop via segments
            self.create_snake()

        def create_snake(self):
            for position in STARTING_POSITIONS:
                new_segment = Turtle("square")
                new_segment.color("white")
                new_segment.penup() # Fixes the weird thin line between segments when snake moves
                new_segment.goto(position)
                self.segments.append(new_segment)

        def move(self):
            for seg_num in range(len(self.segments) - 1, 0, -1):  # Move each snake segment
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(MOVE_DISTANCE)
    ```

  - **`main.py`**
    ```python
    import time
    from turtle import Screen

    from snake import Snake

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()

    game_is_on = True
    while game_is_on:
        screen.update()         # Refresh screen btwn snake movements
        time.sleep(0.1)         # Adds delay btwn movements before screen refresh

        snake.move()
    
    screen.exitonclick()
    ```

---

## Update 3: Controlling the Snake
**Date:** 20250120

- **Objective:** Implement keyboard controls to change the snake's direction.
- **Steps Completed:**
  1. Configured the game to listen for keyboard inputs using `screen.listen()`.
  2. Added key bindings to control the snake's direction using the arrow keys.
  3. Updated the `Snake` class with methods to handle directional changes (`move_up`, `move_down`, `move_left`, `move_right`).
  4. Incorporated conditional logic to prevent the snake from reversing direction.
- **Code Highlights:**
  - **`main.py`**
    ```python
    screen.listen()
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")
    ```

  - **`snake.py`**
    ```python
    UP = 90
    DOWN = 270
    LEFT = 180
    RIGHT = 0

    class Snake:
        ...

        def move_up(self):
            if self.head.heading() != DOWN:
                self.segments[0].setheading(UP)

        def move_down(self):
            if self.head.heading() != UP:
                self.segments[0].setheading(DOWN)

        def move_left(self):
            if self.head.heading() != RIGHT:
                self.segments[0].setheading(LEFT)

        def move_right(self):
            if self.head.heading() != LEFT:
                self.segments[0].setheading(RIGHT)
    ```


---

## Update 4: Detecting Collision with Food

**Date**: 20250203

- **Objective**: Implement food spawning and collision detection with the snake.
- **Steps Completed**:
  1.	Created a Food class in a new food.py file.
  2.	Utilized class inheritance by making Food a subclass of the Turtle class.
  3.	Overrode the __init__ method of Turtle to customize the appearance and behavior of the food.
  4.	Implemented the refresh() method to randomly reposition the food on the screen upon collision detection.
  5.	Integrated food collision detection into main.py using the distance() method from the Turtle class.

####	Understanding Class Inheritance in Food Class:
The Food class inherits from the Turtle class, allowing it to use all the built-in methods and attributes of a Turtle object while modifying its behavior specifically for food mechanics.

#### How Inheritance Works Here:
-	The `super().__init__()` call invokes the constructor of the parent Turtle class, initializing the food object as a Turtle.
-	By inheriting from Turtle, the Food class gains access to all Turtle methods, such as `.shape()`, `.penup()`, `.color()`, `.goto()`, and `.speed()`.
-	The Food class customizes these properties to make the food appear as a small, blue circle and move instantly when repositioned.

#### Code Highlights

- [NEW] **`food.py`** (Creating the Food Class with Inheritance)
  ```py
  from turtle import Turtle
  import random

  class Food(Turtle):  # Inherits from Turtle class
      def __init__(self):
          super().__init__()  # Calls the Turtle class constructor
          self.shape("circle")  
          self.penup()  # Prevents food from drawing lines  
          self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Makes food smaller  
          self.color("blue")  
          self.speed("fastest")  # Instantly moves when repositioned  
          self.refresh()  # Places food at a random location when initialized  

      def refresh(self):
          """Moves food to a new random location within the game boundaries."""
          random_x = random.randint(-280, 280)
          random_y = random.randint(-280, 280)
          self.goto(random_x, random_y)  # Uses Turtle's built-in .goto() method
  ```

- [MODIFIED] **`main.py`** (Detecting Collision with Food and Repositioning It)

  ```py
  # Create an instance of the Food class
  food = Food()

  # Inside the game loop, check for collision with food
  if snake.head.distance(food) < 15:  # If the snake's head is within 15 pixels of food
      print("nom nom nom")  # Placeholder for future scorekeeping
      food.refresh()  # Moves food to a new random location
  ```


#### Key Takeaways from this Update:
-	The Food class is a subclass of Turtle, inheriting all of its attributes and methods.
-	The `super().__init__()` method ensures that the Food object is properly initialized as a Turtle instance.
-	The `.refresh()` method allows the food to respawn at a new random location whenever the snake eats it.
-	The `distance()` method from Turtle is used to detect when the snake collides with food.


---

## Update 5: Adding a Scoreboard and Detecting Collisions

#### Date: 20250220

- **Objective:** Implement a scoring system and begin handling collisions with walls.

- **Steps Completed:**
  1. Created a new Scoreboard class in a separate scoreboard.py file.
  2. Displayed the score dynamically on the screen using Turtle’s write() method.
  3. Increased the score whenever the snake successfully eats food.
  4. Began setting up collision detection with screen boundaries (logic to be completed).


#### Code Highlights:

-	[NEW] `scoreboard.py`

    ```py
    from turtle import Turtle

    class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color("white")
            self.penup()
            self.hideturtle()
            self.goto(0, 270)
            self.update_score()

        def update_score(self):
            self.clear()
            self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

        def increase_score(self):
            self.score += 1
            self.update_score()
    ```

-	[UPDATED] `main.py` 

    ```py
    from scoreboard import Scoreboard

    scoreboard = Scoreboard()

    if snake.head.distance(food) < 15:
        print("*nom nom nom*")
        scoreboard.increase_score()
        food.refresh()
    ```


---
## Update 6: Collision Detection with Walls (Game Over Condition)

#### Date: 20250222

- **Objective:** End the game when the snake collides with the wall.

- **Steps Completed:**
  1. Added logic to detect when the snake's head crosses the screen boundaries.
  2. Displayed a "GAME OVER" message both on-screen and in the console.
  3. Integrated the collision detection within the main game loop.

- **Code Highlights:**

  - **`main.py`**
    ```python
    # main.py
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    ```

  - **`scoreboard.py`**
    ```py
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        print(f"GAME OVER. Final Score: {self.score}")
    ```

---
## Final Update (Step 7)
- Extend the snake’s body each time it eats food.
- Implement collision detection with the snake’s own tail.
