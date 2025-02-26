from turtle import Screen, Turtle

# * 1. Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.title("Pong - Arcade Video Game")
screen.tracer(0)            # ? Disables automatic screen updates for smoother animation control.

"""
The .tracer(0) method prevents unnecessary animations when moving objects.
By default, Turtle automatically updates the screen whenever an object moves,
which can cause a noticeable delay. Disabling this feature allows manual
screen updates using .update(), ensuring smoother movement.
"""

# * 2. Create and Move Paddle via Key Presses

paddle = Turtle("square")   # Alternatively, use paddle.shape("square") separately.

"""
About .shapesize():
By default, Turtle shapes are 20x20 pixels. The .shapesize() method scales
the shape based on a stretch factor.

Formula:
    Final Width  = 20 x stretch_len
    Final Height = 20 x stretch_wid

Applying .shapesize(stretch_wid=5, stretch_len=1) results in:
    Width  = 20 x 1  = 20 pixels
    Height = 20 x 5  = 100 pixels
Thus, the paddle dimensions become 100x20 pixels.
"""
paddle.shapesize(stretch_wid=5, stretch_len=1, outline=None)
paddle.color("#fff")
paddle.penup()
paddle.goto(350, 0)

# ? Functions to move the paddle up and down
def go_up():
    paddle.goto(paddle.xcor(), paddle.ycor() + 20)

def go_down():
    paddle.goto(paddle.xcor(), paddle.ycor() - 20)

screen.listen()             # ? Enable keypress detection
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True           # ? Game loop to manually refresh the screen
while game_is_on:
    screen.update()

# * Upcoming Features:
# * 3. Create Another Paddle with a Class
# * 4. Create a Ball and Make it Move
# * 5. Ball Bounce Logic: Detect Collision with Wall
# * 6. Detect Collision with Paddle
# * 7. Detect When Ball Goes out of Bounds
# * 8. Score Keeping and Adjusting Ball Speed

screen.exitonclick()
