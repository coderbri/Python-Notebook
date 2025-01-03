from turtle import Turtle, Screen

# Create a Turtle object named 'tim'
tim = Turtle()

# Create a Screen object to display the Turtle graphics
screen = Screen()

# Define a function to move the turtle forward by 10 steps
def move_forwards():
    tim.forward(10)

# Set up the screen to listen for user events (key presses, clicks, etc.)
screen.listen()  # Activates event listening for user interactions

# Bind the spacebar key to the move_forwards function
# When the user presses the spacebar, the move_forwards function is called
screen.onkey(key="space", fun=move_forwards)

# Keep the window open and wait for the user to click to close it
screen.exitonclick()  # Closes the Turtle graphics window when clicked
