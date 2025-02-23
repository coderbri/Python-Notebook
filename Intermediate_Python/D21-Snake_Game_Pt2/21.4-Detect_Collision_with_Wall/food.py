from turtle import Turtle
import random

class Food(Turtle): # ? Inherit all the capabilities of the Turtle Class

    # Spawn Food appearance and random appearance
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        # ? these dimensions will prevent the food from spawning too close to the wall
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
