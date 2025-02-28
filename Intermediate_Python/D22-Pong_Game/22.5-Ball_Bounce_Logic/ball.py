from turtle import Turtle

# * 4. Create a Ball and Make it Move
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

    # * 5. Ball Bounce Logic: Detect Collision with Wall
    def bounce(self):
        """
        Reverses the ball's vertical direction when it collides with the top or bottom wall.

        - If the ball was moving **upward** (positive `y_move`), it will now move **downward**.
        - If the ball was moving **downward** (negative `y_move`), it will now move **upward**.
        - This is done by multiplying `y_move` by `-1`, effectively flipping its sign.
        """
        self.y_move *= -1
