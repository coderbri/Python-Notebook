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


<!-- TODO:
---

## Update 6: Detect Collision with Paddle
- add date
- add objective
- add steps made in the project
    - also explain the logic needed to be taken into account to ensure proper bounce logic from the paddle
    - also explain the modification made to the bounce method by splitting the bounce logic to be one regarding just among the y-axis and x-axis, respectively
- add code highlights

#### `main.py`
```py
 # * 5. Ball Bounce Logic: Detect Collision with Wall
    # ? Reverse direction when the ball hits the top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() # ? changed from .bounce to .bounce_y

    # * 6. Detect Collision with Paddle
    # this logic calls for taking into account edge cases in which the ball may
    # not always hit the paddle directly in the center but on the edges. To take
    # that into account, we cannot measure the distance within less than the 20 pixels.
    # Instead we can solve this problem by adding an additional condition in which if
    # the ball has gone past a certain point on the x-axis (going far enough to the
    # right) and its within a 50 pixel distance of the paddle, then that means the ball
    # has hit the paddle
    if (
            ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        print("Made contact!") # test first that the hit can be detected
        # after confirming that contact has been made, we can make the ball bounce but among the x-axis
        ball.bounce_x()
```

#### `ball.py`
```py
    # * 5. Ball Bounce Logic: Detect Collision with Wall
    def bounce_y(self):
        """Reverses the ball's vertical direction when it collides with the top or bottom wall."""
        self.y_move *= -1

    # * 6. Detect Collision with Paddle
    # we'll need another method that will make the ball bounce within the x-axis upon paddle contact
    def bounce_x(self):
        self.x_move *= -1
```
-->

<!-- TODO:
---

## Update 7: Detect When Ball Goes out of Bounds
- add date
- add objective
- add steps made in the project
- add code highlights

-->

---

## Upcoming Features:

- [x] 1. Main Screen Setup
- [x] 2. Create and Move Paddle via Key Presses
- [x] 3. Create Another Paddle with a Class
- [x] 4. Create a Ball and Make it Move
- [x] 5. Ball Bounce Logic: Detect Collision with Wall
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
