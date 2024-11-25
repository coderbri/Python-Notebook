from turtle import Turtle, Screen

# * Declaring a turtle object
timmy = Turtle()
print(timmy)                #  <turtle.Turtle object at 0x104f85310>

# * Using Methods
timmy.shape("turtle")       # ? turns timmy from pointer into turtle
timmy.color("darkslategray4")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight) #  300
my_screen.exitonclick()     # ? screen will no longer quickly exit
