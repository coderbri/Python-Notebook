from turtle import Turtle
import random

class Food(Turtle):
    """Represents food for the snake, inheriting from Turtle."""

    def __init__(self):
        """Initializes food properties and spawns it in a random location."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Makes food smaller
        self.color("blue")
        self.speed("fastest")  # Ensures instant movement when repositioned
        self.refresh()  # Places food at a random position on creation

    def refresh(self):
        """Moves food to a new random location on the screen."""
        random_x = random.randint(-280, 280)  # Prevents spawning too close to walls
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)