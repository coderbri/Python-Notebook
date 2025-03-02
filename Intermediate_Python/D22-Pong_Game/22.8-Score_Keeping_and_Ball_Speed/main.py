import time

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# * 1. Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("#000")
screen.title("Pong - Arcade Video Game")
screen.tracer(0)        # ? Disables automatic screen updates for smoother animation control.

# * 3. Create Another Paddle with a Class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# * 4. Create a Ball and Make it Move
ball = Ball()           # ? Ball starts at (0,0)

# * 8.1 Setting up Scoreboard
scoreboard = Scoreboard()

# * 2. Create and Move Paddle via Key Presses
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
'''
Fix for paddle responsiveness:
The "W" and "S" keys moved the paddle in smaller increments compared to the arrow keys.
Using `onkeypress()` instead of `onkey()` ensures immediate response for both players.
'''

game_is_on = True
while game_is_on:
    # * 8.2 Adjusting Ball Speed
    time.sleep(ball.move_speed)     # ? Uses dynamic speed instead of a fixed delay.
    screen.update()                 # ? Manually updates the screen for smooth animation
    ball.move()                     # ? Moves the ball in a diagonal direction

    # * 5. Ball Bounce Logic: Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280: # ? Reverse direction when the ball hits the top or bottom wall
        ball.bounce_y()

    # * 6. Detect Collision with Paddle
    if (
            ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()             # ? Bounce in the x direction after paddle contact

    # * 7-8. Detect When Ball Goes out of Bounds and Score Keeping
    '''
    If a paddle fails to return the ball, the opponent gains a point.
    The ball resets to the center and moves toward the scoring player.
    '''
    if ball.xcor() > 380:           # ? Right paddle missed
        ball.reset_position()
        scoreboard.increment_l_points()

    if ball.xcor() < -380:          # ? Left paddle missed
        ball.reset_position()
        scoreboard.increment_r_points()


screen.exitonclick()
