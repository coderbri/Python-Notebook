## Challenge 5: Make Turtle do a Random Walk with Random RGB Colors

This code generates a **random walk** with randomly generated **RGB colors** using Python's `turtle` library. The `colormode(255)` enables RGB color mode, and the `generate_random_color` function creates a random color tuple `(r, g, b)` where each value is between 0 and 255. The turtle (`timmy`) moves forward in 30-unit segments, randomly choosing one of four directions: east (0°), north (90°), west (180°), or south (270°). The pen size is set to 10 for thicker lines, and the speed is set to "fastest" for quick drawing. The result is a colorful, random path displayed on the screen until the user clicks to exit.

![Demo of Challenge 5](./challenge5.gif)
