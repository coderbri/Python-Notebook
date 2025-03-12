## Features Implemented

- [x] 1. Main Game Setup

- [x] 2. Create the Player Behavior
<!-- Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move the turtle north. -->

- [x] 3. Create the Car Behavior
<!-- Create cars that are 20px high by 40px wide that are randomly generated along the y-axis and move to the left edge of the screen. No cars should be generated in the top and bottom 50px of the screen (think of it as a safe zone for our little turtle). Hint: generate a new car only every 6th time the game loop runs. -->

- [x] 4. Detect when the Turtle Collides with a Car (Game Over Logic)
<!-- Detect when the turtle player collides with a car and stop the game if this happens. -->

- [x] 5. Detect when the Player has reached the other side
<!-- Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the starting position and increase the speed of the cars. Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed. -->

- [x] 6. Add the Scoreboard and Game Over Sequence
<!-- Create a scoreboard that keeps track of which level the user is on. Every time the turtle player does a successful crossing, the level should increase. When the turtle hits a car, GAME OVER should be displayed in the centre. -->