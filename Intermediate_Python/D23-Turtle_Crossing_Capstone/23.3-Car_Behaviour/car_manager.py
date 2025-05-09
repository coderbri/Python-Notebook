import random
from turtle import Turtle

# Constants for car behavior
COLORS = ["#FCC1C1", "#FCDFC1", "#FCFCC1", "#C1FCDF", "#C1E0FC", "#C1C2FC"]  # Car fill colors
COLORS_OUTLINE = ["red", "orange", "goldenrod", "green", "blue", "purple"]   # Car outline colors
STARTING_MOVE_DISTANCE = 5  # Initial speed of the cars
MOVE_INCREMENT = 10         # Speed increase per level

class CarManager:
    """Manages the creation and movement of cars in the Turtle Crossing game."""

    def __init__(self):
        """Initialize the CarManager with an empty list of cars."""
        self.all_cars = []

    def create_car(self):
        """Randomly generates a car and adds it to the game.  
        A new car is created only 1 out of every 6 game loops to prevent overcrowding.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Limits car creation frequency
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Resize to 20x40 px
            new_car.penup()
            new_car.color(random.choice(COLORS_OUTLINE), random.choice(COLORS))
            
            # Generate a random y-coordinate within safe bounds (-225 to 225)
            random_y = random.randint(-225, 225)
            new_car.goto(300, random_y)  # Cars start from the right edge
            
            self.all_cars.append(new_car)  # Add to car list

    def move_cars(self):
        """Moves all cars leftward across the screen."""
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)  # Move each car left by 5 pixels