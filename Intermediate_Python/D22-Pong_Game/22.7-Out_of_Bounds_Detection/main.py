import time

from turtle import Screen
from paddle import Paddle
from ball import Ball

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

# * 2. Create and Move Paddle via Key Presses
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)     # ? Slows down the game loop to control ball speed
    screen.update()     # ? Manually updates the screen for smooth animation
    ball.move()         # ? Moves the ball in a diagonal direction

    # * 5. Ball Bounce Logic: Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280: # ? Reverse direction when the ball hits the top or bottom wall
        ball.bounce_y()

    # * 6. Detect Collision with Paddle
    if (
            ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320
    ):
        ball.bounce_x()     # ? Bounce in the x direction after paddle contact

    # * 7. Detect When Ball Goes out of Bounds
    '''
    If a paddle fails to return the ball, the opponent scores a point.
    The ball then resets to the center and moves in the opponent’s direction.
    
    The screen width is 800, and paddles are positioned around ±350.
    Since the paddle width ranges from ±340 to ±360, if the ball reaches ±380,
    it is considered out of bounds.
    '''
    if ball.xcor() > 380:   # ? Right paddle missed
        ball.reset_position()

    if ball.xcor() < -380:  # ? Left paddle missed
        ball.reset_position()

# * 8. Score Keeping and Adjusting Ball Speed

screen.exitonclick()
