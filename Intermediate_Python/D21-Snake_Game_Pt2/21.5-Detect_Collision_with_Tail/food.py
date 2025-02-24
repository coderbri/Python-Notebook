from turtle import Turtle
import random

class Food(Turtle):
    """
    Represents the food object for the Snake Game.
    Inherits from the Turtle class to utilize drawing and movement capabilities.
    Spawns food in a random location on the screen, ensuring it's not too close to the walls.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Places the food at a new random position on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
