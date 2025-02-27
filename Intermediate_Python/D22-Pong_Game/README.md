# Pong - Classic Arcade Game: Update Log

## Project Overview

<!-- TODO: To be filled out later -->

## Update 1: Main Screen Setup
**Date:** 20250225

- **Objective:** Set up the main screen for the Pong game using the `turtle` module.

#### Steps Completed:
- Initialized the game window using the `Screen` class.
- Set the screen dimensions to **800x600 pixels**.
- Changed the background color to **black** (`#000`) for a classic arcade feel.
- Updated the window title to **"Pong - Arcade Video Game"**.
- Implemented `screen.exitonclick()` to keep the window open until clicked.

### Code Highlights:
```python
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.title("Pong - Arcade Video Game")

screen.exitonclick()
```

---

## Update 2: Create and Move Paddle via Key Presses  
**Date:** 20250225

- **Objective:** Create a paddle and enable movement using key presses.  

#### Steps Completed:
- Created a paddle using the `Turtle` class and set its shape to a rectangle.  
- Adjusted the paddle size using `.shapesize(stretch_wid=5, stretch_len=1)`, making it **100x20 pixels**.  
- Removed the paddle’s default pen behavior using `.penup()`.  
- Positioned the paddle at **(350, 0)** on the right side of the screen.  
- Defined `go_up()` and `go_down()` functions to move the paddle **20 pixels up and down**.  
- Enabled keypress detection using `.listen()` and `.onkey()` for the **Up** and **Down** arrow keys.  
- Used `screen.tracer(0)` to disable automatic animations and implemented a **while loop with `screen.update()`** to manually refresh the screen, ensuring smooth movement.

### Explanation of Key Methods:  

#### `.tracer(n, delay)` (Screen Method)  
The `.tracer(0)` method disables automatic screen updates, allowing manual control over rendering. This helps optimize animations and prevents flickering when moving objects.  

- Normally, `turtle` updates the screen every time an object moves, which can cause **unnecessary transition animations**.  
- Setting `.tracer(0)` **stops automatic updates**, keeping the screen static until manually refreshed.  
- To display movement properly, `.update()` is used inside a game loop, ensuring smooth rendering.

#### `.shapesize(stretch_wid, stretch_len, outline)` (Turtle Method)  
The `.shapesize()` method resizes the paddle by **scaling its default 20x20 pixel size**.  

<!-- ! REQUIRED KaTeX plugin to see equation:
- **Stretching logic:**
    - $$ \text{Final Width} = 20 \times \text{stretch_len} $$
    - $$ \text{Final Height} = 20 \times \text{stretch_wid} $$
The final width is given by $ 20 \times \text{stretch_len} $.
-->

- **Stretching logic:**
    - **Final Width** = `20 × stretch_len`
    - **Final Height** = `20 × stretch_wid`
    - `stretch_wid=5` → Paddle becomes 100 pixels tall (20 × 5).
    - `stretch_len=1` → Paddle remains 20 pixels wide (20 × 1).
    - The optional outline parameter controls the shape’s border thickness (set to `None` here).

```python
paddle.shapesize(stretch_wid=5, stretch_len=1)
```

### Code Highlights

```py
from turtle import Screen, Turtle

screen.tracer(0)

paddle = Turtle("square")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color("#fff")
paddle.penup()
paddle.goto(350, 0)

def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)

def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
```

---

## Update 3: Create Another Paddle with a Class

**Date:** 20250225  

- **Objective:** Refactor the code by creating a `Paddle` class to handle paddle-related logic and enable the creation of multiple paddles, improving modularity and readability.

### Steps Completed:
- **Encapsulated paddle logic** into a separate `Paddle` class inside `paddle.py`, making the code more reusable.
- **Utilized class inheritance** by extending the `Turtle` class, eliminating the need to manually instantiate a `Turtle` object within the paddle setup.
- **Replaced hardcoded paddle creation** in `main.py` with `Paddle` objects, allowing for dynamic positioning and easy scalability.
- **Refactored movement functions** into the `Paddle` class to keep paddle behavior encapsulated.
- **Added key bindings** for both the right (`Up`, `Down`) and left (`W`, `S`) paddles in `main.py`.

### Code Highlights:

#### `paddle.py`
```py
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("#fff")
        self.penup()
        self.goto(position)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
```

#### `main.py`
```py
from paddle import Paddle

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
```

---


## Update 4: Create a Ball and Make it Move
**Date:** 20250226

- **Objective:** Introduce a `Ball` class to manage the ball’s movement and behavior in the game, using class inheritance for cleaner code structure.

### Steps Completed:
- **Created a `Ball` class** in `ball.py`, inheriting from `Turtle`, which simplifies the ball’s creation and movement.
- **Set the ball’s default properties**: assigned a `"circle"` shape, white color (`"#fff"`), and enabled `penup()` to remove unnecessary drawing trails.
- **Implemented ball movement logic** in the `move()` method, which updates the ball’s `(x, y)` position by `+10` pixels per iteration.
- **Integrated the ball into `main.py`** and instantiated it at `(0,0)`.
- **Controlled animation speed** by adding `time.sleep(0.1)` in the game loop, slowing down the ball’s movement efficiently instead of adjusting pixel increments.
- **Current Limitation:** The ball currently moves in a diagonal direction indefinitely and flies out of bounds. This issue will be addressed in the next checkpoint.

### Code Highlights:

#### `main.py`

```py
import time
from ball import Ball

ball = Ball() # ? starting position is in (0, 0)

game_is_on = True
while game_is_on:
    time.sleep(0.1) # ? Slows down the game loop to control ball speed
    screen.update() # ? Manually updates the screen for smooth animation
    ball.move() # ? Moves the ball in a diagonal direction

```

#### `ball.py`

```py
from turtle import Turtle

# * 4. Create a Ball and Make it Move
class Ball(Turtle):

    def __init__(self):
        """Initializes the ball at the center of the screen with default properties."""
        super().__init__()
        self.color("#fff")
        self.shape("circle")
        self.penup()

    def move(self):
        """Moves the ball diagonally by updating its x and y coordinates."""
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

```

Note: No changes were made to `paddle.py`.

---

<!-- TODO:
## Update 5: Ball Bounce Logic – Detect Collision with Wall
- add date
- add objective
- add steps made in the project
- add code highlights
-->

#### `main.py`

```py
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # * 5. Ball Bounce Logic: Detect Collision with Wall
    # to create collision+bounce logic, 300 is half of 600 so when the ball is
    # above/below 300 (we'll set it at 280 so it doesn't cross the edge of the
    # screen, we can assume that the ball has already hit "the wall", thus we
    # can bounce from that limit
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
```

#### `ball.py`

```py
from turtle import Turtle

# * 4. Create a Ball and Make it Move
class Ball(Turtle):

    def __init__(self):
        """Initializes the ball at the center of the screen with default properties."""
        super().__init__()
        self.color("#fff")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # ... move logic

    def bounce(self):
        # we need to first figure out a new y coordinate coz originally,
        # the y coordinate is going up until it hits a wall where y now
        # needs to be reversed (if originally increasing, then it needs
        # to decrease and vice versa). we can resolve this by creating
        # an attribute that defines the coordinate distance the ball will bounce
        self.y_move *= -1
```


## Upcoming Features:

- [x] 1. Main Screen Setup
- [x] 2. Create and Move Paddle via Key Presses
- [x] 3. Create Another Paddle with a Class
- [x] 4. Create a Ball and Make it Move
- [ ] 5. Ball Bounce Logic: Detect Collision with Wall
- [ ] 6. Detect Collision with Paddle
- [ ] 7. Detect When Ball Goes out of Bounds
- [ ] 8. Score Keeping and Changing Ball Speed

---

## Acknowledgments

Inspired by classic arcade games and built as part of a Python learning journey through Dr. Angela Yu’s **100 Days of Code: Python Pro Bootcamp.**

---
<section align="center">
  <code>coderBri © 2025</code>
</section>
