from turtle import Turtle

# * 4. Create a Ball and Make it Move
class Ball(Turtle):

    def __init__(self):
        """Initializes the ball at the center of the screen with default properties."""
        super().__init__()
        self.color("#fff")
        self.shape("circle")
        self.penup()
        self.x_move = 10        # ? x_move (int): The horizontal movement step size.
        self.y_move = 10        # ? y_move (int): The vertical movement step size.
        self.move_speed = 0.1   # ? Default ball speed, gradually increases upon paddle collision.

    def move(self):
        """Moves the ball diagonally by updating its x and y coordinates.
        The direction is determined by the current values of x_move and y_move."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # * 5. Ball Bounce Logic: Detect Collision with Wall
    def bounce_y(self):
        """Reverses the ball's vertical direction when it collides with the top or bottom wall."""
        self.y_move *= -1

    # * 6. Detect Collision with Paddle
    def bounce_x(self):
        """Reverses the ball's horizontal direction when it collides with a paddle and increases speed."""
        self.x_move *= -1
        self.move_speed *= 0.9  # ? Ball speeds up by 10% upon hitting a paddle.

    # * 7. Detect When Ball Goes out of Bounds
    def reset_position(self):
        """Resets the ball to the center, restores default speed, and reverses direction."""
        self.goto(0, 0)
        self.move_speed = 0.1   # ? Resets speed to prevent indefinite acceleration.
        self.bounce_x()
