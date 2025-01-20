# Snake Game: Update Log

## Project Overview
This repository documents the development of a Snake Game built using Python and the Turtle module. Each update corresponds to a significant milestone in the creation of the game, showcasing progressive implementation of features and functionality.

---

### Update 1: Setting Up the Screen and Creating the Snake
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

### Update 2: Moving the Snake
**Date:** 20250119

- **Objective:** Enable the snake to move continuously in the game space.
- **Steps Completed:**
  1. Implemented a list to store the snake segments for movement tracking.
  2. Configured a game loop using `while` to update the screen and move the snake.
  3. Added functionality for each segment to follow the one in front, simulating snake movement.
  4. Introduced a slight delay between screen updates to create a smooth movement effect.
- **Code Highlights:**
  ```python
  screen.tracer(0)    # Stops constant screen refresh
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

### Update 2.5: Modularization with the Snake Class
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

### Upcoming Updates
- **Step 3:** Control the Snake
- **Step 4:** Detect Collision with Food
- **Step 5:** Create a Scoreboard
- **Step 6:** Detect Collision with Wall
