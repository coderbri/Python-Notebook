## Challenge 6: Use Turtle to Draw a Spirograph

This code generates a **spirograph** using Python's `turtle` library, where circles are drawn at incremental angles to form a mesmerizing pattern. The `colormode(255)` is enabled for RGB colors, and the `generate_random_color` function creates a random `(r, g, b)` color tuple. The `draw_spirograph` function accepts a `size_of_gap` parameter, determining the angle increment between each circle. The turtle (`timmy`) draws a circle of radius 100, then adjusts its heading by the specified gap size until completing a full rotation (360 degrees). The speed is set to "fastest" for efficient drawing, resulting in a colorful, circular spirograph design displayed until the user clicks to exit.

![Demo of Challenge 6](./challenge6.gif)
