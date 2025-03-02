# Pong - Classic Arcade Game: Update Log

<!-- TODO: To be filled out later 

## Project Overview
-->

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

## Update 5: Ball Bounce Logic – Detect Collision with Wall
**Date:** 20250227

- **Objective:** Implement ball collision detection with the top and bottom walls, ensuring the ball bounces upon impact.

### Steps Taken
- Defined `x_move` and `y_move` attributes in the `Ball` class to manage movement direction.  
- Implemented the `move()` method to update the ball’s position diagonally using `x_move` and `y_move`.  
- Added a `bounce()` method that **reverses the ball’s vertical movement (`y_move *= -1`)** when it collides with the walls.  
- Set the collision boundary at `y = ±280` to prevent the ball from partially clipping outside the screen.  
- Updated the game loop in `main.py` to check if the ball’s y-coordinate exceeds ±280 and trigger `bounce()`.  

### Code Highlights  

#### `main.py`

```py
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # * 5. Ball Bounce Logic: Detect Collision with Wall
    '''
    The screen height is 600 pixels, so the top and bottom edges are at ±300.
    To prevent the ball from visually clipping outside the screen, we set 
    the bounce threshold at ±280. If the ball's y-coordinate exceeds this limit,
    it indicates a collision, and we call the bounce() method to reverse direction.
    '''
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
```

#### `ball.py`

```py
class Ball(Turtle):
    
    def __init__(self):
        """Initializes the ball at the center of the screen with default properties."""
        super().__init__()
        self.color("#fff")
        self.shape("circle")
        self.penup()
        self.x_move = 10    # ? x_move (int): The horizontal movement step size.
        self.y_move = 10    # ? y_move (int): The vertical movement step size.

    def move(self):
        """
        Moves the ball diagonally by updating its x and y coordinates.
        The direction is determined by the current values of x_move and y_move.
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        """
        Reverses the ball's vertical direction when it collides with the top or bottom wall.

        - If the ball was moving **upward** (positive `y_move`), it will now move **downward**.
        - If the ball was moving **downward** (negative `y_move`), it will now move **upward**.
        - This is done by multiplying `y_move` by `-1`, effectively flipping its sign.
        """
        self.y_move *= -1
```

---

## Update 6: Detect Collision with Paddle
**Date:** 20250228

- **Objective:** Implement logic to detect when the ball collides with a paddle and ensure it bounces properly along the x-axis.

### Steps Taken
- **Refactored the bounce logic:**
    - Previously, the `bounce()` method handled all bouncing logic, but now it is split into two separate methods:
        - `bounce_y()`: Handles bouncing when the ball collides with the top or bottom walls.
        - `bounce_x()`: Handles bouncing when the ball collides with a paddle.
- **Implemented paddle collision detection:**
    - The ball should bounce off the paddles only if:
        - It moves far enough along the x-axis (past ±320).
        - It is within **50 pixels** of the paddle’s position (to account for edge cases where the ball might hit near the paddle’s edges).
- **Tested paddle collision detection:**
    - Printed `"Made contact!"` when the ball successfully hit a paddle to confirm detection before implementing the bounce effect.

### Code Highlights

#### `main.py`

```py
# * 5. Ball Bounce Logic: Detect Collision with Wall
# ? Reverse direction when the ball hits the top or bottom wall
if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()  # ? Changed from .bounce() to .bounce_y()

# * 6. Detect Collision with Paddle
if (
        ball.distance(r_paddle) < 50 and ball.xcor() > 320
        or ball.distance(l_paddle) < 50 and ball.xcor() < -320
):
    print("Made contact!")  # Test detection first
    ball.bounce_x()         # Bounce in the x direction after paddle contact
```

#### `ball.py`

```py
# * 5. Ball Bounce Logic: Detect Collision with Wall
def bounce_y(self):
    """Reverses the ball's vertical direction when it collides with the top or bottom wall."""
    self.y_move *= -1

# * 6. Detect Collision with Paddle
def bounce_x(self):
    """Reverses the ball's horizontal direction when it collides with a paddle."""
    self.x_move *= -1
```

---

## Update 7: Detect When Ball Goes out of Bounds
**Date:** 20250228

- **Objective:** Implement logic to detect when the ball goes out of bounds, ensuring that when a paddle fails to return the ball, the opponent is awarded a point, and the ball resets for the next round.

### Steps Taken
- **Defined out-of-bounds detection:**
    - The game screen has a width of **800 pixels**, with paddles positioned around **±350** on the x-axis.
    - Since each paddle extends from approximately **±340 to ±360**, if the ball moves beyond **±380**, it has officially gone out of bounds.
- **Implemented reset behavior:**
    - When the ball crosses **+380** on the x-axis, the **right paddle missed** the ball.
    - When the ball crosses **-380** on the x-axis, the **left paddle missed** the ball.
    - In either case, the ball **resets to the center** of the screen and reverses direction, ensuring it moves toward the opponent’s side.

### Code Highlights

#### `main.py`

```py
while game_is_on:
    # * 7. Detect When Ball Goes out of Bounds
    if ball.xcor() > 380:   # ? Right paddle missed
        ball.reset_position()

    if ball.xcor() < -380:  # ? Left paddle missed
        ball.reset_position()
```

#### `ball.py`

```py
class Ball(Turtle):
    # * 7. Detect When Ball Goes out of Bounds
    def reset_position(self):
        """Resets the ball to the center of the screen and reverses its horizontal direction."""
        self.goto(0, 0)
        self.bounce_x()
```

---

## Update 8: Score Keeping and Changing Ball Speed
**Date:** 20250301

- **Objective:** Enhance gameplay by implementing a scoreboard to track player scores and introducing dynamic ball speed adjustments for a more challenging experience.

### Steps Taken
- **Implemented scorekeeping:**
    - Created a `Scoreboard` class to track each player’s score.
    - The score updates dynamically on the screen whenever a player misses the ball.
- **Adjusted ball speed dynamically:**
    - Instead of setting the ball’s speed directly in `time.sleep()`, initialized it with a `move_speed` attribute.
    - Each time the ball hits a paddle, its speed **increases by 10%**, making the game progressively harder.
    - When the ball goes out of bounds, its speed **resets to default**, preventing indefinite acceleration.
- **(Debugging) Fixed paddle responsiveness issue:**
    - The "w" and "s" keys initially responded slower than the "Up" and "Down" arrow keys.
    - **Solution:** Changed `onkey()` to `onkeypress()`, ensuring key presses are registered immediately for both players.

### Code Highlights

#### `main.py`

```py
from scoreboard import Scoreboard

# * 8.1 Setting up Scoreboard
scoreboard = Scoreboard()

screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
'''
Fix for paddle responsiveness:
The "W" and "S" keys moved the paddle in smaller increments compared to the arrow keys.
Using `onkeypress()` instead of `onkey()` ensures immediate response for both players.
'''

while game_is_on:
    # * 8. Adjusting Ball Speed
    time.sleep(ball.move_speed)  # Uses dynamic speed instead of a fixed delay.

    # * 7-8. Detect When Ball Goes out of Bounds and Score Keeping
    '''
    If a paddle fails to return the ball, the opponent gains a point.
    The ball resets to the center and moves toward the scoring player.
    '''
    if ball.xcor() > 380:  # ? Right paddle missed
        ball.reset_position()
        scoreboard.increment_l_points()

    if ball.xcor() < -380:  # ? Left paddle missed
        ball.reset_position()
        scoreboard.increment_r_points()
```

#### `ball.py`

```py
class Ball(Turtle):
    def __init__(self):
        """Initializes the ball with a default speed and movement attributes."""
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # ? Default ball speed, gradually increases upon paddle collision.

    def bounce_x(self):
        """Reverses the ball's horizontal direction when it collides with a paddle and increases speed."""
        self.x_move *= -1
        self.move_speed *= 0.9  # ? Ball speeds up by 10% upon hitting a paddle.

    def reset_position(self):
        """Resets the ball to the center, restores default speed, and reverses direction."""
        self.goto(0, 0)
        self.move_speed = 0.1  # ? Resets speed to prevent indefinite acceleration.
        self.bounce_x()
```

#### `scoreboard.py`

```py
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier New", 80, "normal")

# * 8. Score Keeping and Adjusting Ball Speed
class Scoreboard(Turtle):

    def __init__(self):
        """Initializes the scoreboard, tracks scores for both players, and displays the initial score."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        # ? Separate attributes for left and right player scores
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and updates the screen with the latest scores."""
        self.clear()
        self.goto(-100, 200)  # ? Left player's score position
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)  # ? Right player's score position
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def increment_l_points(self):
        """Increments left player's score and updates the scoreboard."""
        self.l_score += 1
        self.update_scoreboard()

    def increment_r_points(self):
        """Increments right player's score and updates the scoreboard."""
        self.r_score += 1
        self.update_scoreboard()
```

---

## Acknowledgments

Inspired by classic arcade games and built as part of a Python learning journey through Dr. Angela Yu’s **100 Days of Code: Python Pro Bootcamp.**

---
<section align="center">
  <code>coderBri © 2025</code>
</section>
