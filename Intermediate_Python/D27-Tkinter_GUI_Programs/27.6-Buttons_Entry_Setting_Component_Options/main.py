from tkinter import *
# recommended to use it this way if many classes are used as in this learning case.
# however, if there's only a few classes, only the module need to imported

# Window Screen Setup
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label Creation
my_label = Label(text="The quick brown fox jumps over the lazy dog.",
                         font=("Courier", 16, "bold"))
my_label.pack() # to make it appear in the screen


# * Two ways to change text in a label
my_label["text"] = "New text"
my_label.config(text="This is New Text")

# * Button Creation & Functionality
def button_clicked():
    new_text="I got clicked"
    button.config(text=new_text) # Changes the button's text after it's clicked
    print(new_text)

button = Button(text="Click me", command=button_clicked)
button.pack()

# * Entry Component
# An input, effectively
tk_input = Entry(width=10)  # Sets the input field with a width of 10 characters
tk_input.pack()             # Displays the input field on the screen

def change_title_with_input():
    new_text = tk_input.get()                   # Get the text currently in the Entry widget
    my_label.config(text=new_text)              # Update the my_label text with the input
    input_button.config(text="Titled changed!") # Change the button's text

input_button = Button(text="Change Title", command=change_title_with_input)
input_button.pack()


# Starts the Tkinter event loop. This line keeps the window open and responsive to user input.
# It is similar to a 'while True:' loop, continuously listening for events.
# This must be the last line of the script to ensure all widgets are set up before the loop begins.
window.mainloop()
