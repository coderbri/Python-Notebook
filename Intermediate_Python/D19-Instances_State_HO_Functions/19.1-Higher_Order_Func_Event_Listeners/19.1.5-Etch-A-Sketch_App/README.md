# Etch-A-Sketch Turtle App

## Project Overview

This project is a simple Etch-A-Sketch drawing application implemented using Python's Turtle graphics library. The application allows the user to control the movement and orientation of a turtle on the screen using keyboard inputs. Users can move the turtle forwards, backwards, rotate it clockwise or counterclockwise, and even clear the screen to start over.


## Features

- **Directional Movement**: Move the turtle forward (`W`) or backward (`S`).
- **Rotation**: Rotate the turtle counterclockwise (`A`) or clockwise (`D`).
- **Screen Clearing**: Clear the drawing and reset the turtle to the center of the screen (`C`).

## How It Works

1. **Event Listeners**: The program uses event listeners (`onkey`) to bind specific keyboard keys to turtle actions.

2. **Higher-Order Functions**: Functions like `move_forwards`, `move_backwards`, `turn_clockwise`, `turn_counterclockwise`, and `clear_screen` are passed as arguments to the `onkey` method, which executes them when their corresponding keys are pressed.

3. **Screen Setup**: The Turtle graphics screen (`Screen`) is set up to listen for events with the `listen()` method, allowing it to detect key presses.

4. **Turtle Actions**: The turtle's movement and rotation are controlled via its `forward()`, `backward()`, `right()`, and `left()` methods. The screen is cleared using the `clear_screen()` function, which also resets the turtle to its starting position without leaving a trail.


## Usage Instructions

1. Run the Python script in an environment that supports Turtle graphics.

2. Use the following keys to control the turtle:
   - **W**: Move the turtle forward by 10 units.
   - **S**: Move the turtle backward by 10 units.
   - **A**: Rotate the turtle counterclockwise by 10 degrees.
   - **D**: Rotate the turtle clockwise by 10 degrees.
   - **C**: Clear the screen and reset the turtle to the center.

3. Close the application by clicking on the Turtle graphics window.


## Key Code Highlights

- **Directional Movement**:
  ```python
  screen.onkey(key="w", fun=move_forwards)
  screen.onkey(key="s", fun=move_backwards)
  ```

- **Rotation**:
  ```python
  screen.onkey(turn_counterclockwise, "a")
  screen.onkey(turn_clockwise, "d")
  ```

- **Clear Screen**:
  ```python
  def clear_screen():
      tim.clear()         # Clears drawing
      tim.penup()         # Lifts pen to prevent drawing while resetting position
      tim.home()          # Resets turtle to starting position
      tim.pendown()       # Lowers pen for future drawings
  screen.onkey(clear_screen, "c")
  ```


## Learning Objectives

This project was designed to practice the following:
- Implementing event listeners with the `onkey` method.
- Using higher-order functions in Python.
- Manipulating the Turtle graphics library to build interactive applications.
- Binding keyboard inputs to specific behaviors.

---
<section align="center">
  <code>coderBri © 2024</code>
</section>

