import tkinter

# Create the main window, equivalent to `screen = turtle.Screen()` in the Turtle module.
window = tkinter.Tk()
# Set the title of the window.
window.title("My First GUI Program")
# Set the minimum size of the window (width, height).
window.minsize(width=500, height=300)

# Create a Label widget with specified text, font family, size, and weight.
my_label = tkinter.Label(text="The quick brown fox jumps over the lazy dog.",
                         font=("Courier", 16, "bold"))
# Place the label widget in the window. By default, it centers the widget.
# 'side="bottom"' places the label at the bottom of the available space.
# my_label.pack(side="bottom")
my_label.pack()

# Starts the Tkinter event loop. This line keeps the window open and responsive to user input.
# It is similar to a 'while True:' loop, continuously listening for events.
# This must be the last line of the script to ensure all widgets are set up before the loop begins.
window.mainloop()