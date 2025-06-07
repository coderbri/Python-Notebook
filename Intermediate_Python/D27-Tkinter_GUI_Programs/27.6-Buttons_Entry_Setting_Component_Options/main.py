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
my_label.pack()     # to make it appear in the screen


# * Two ways to change text in a label
my_label["text"] = "New text"
my_label.config(text="This is New Text")

# * Button Creation & Functionality
def button_clicked():
    new_text="I got clicked"
    button.config(text=new_text)
    print(new_text)

button = Button(text="Click me", command=button_clicked)
button.pack()

# * Entry Component
# an input, effectively
tk_input = Entry(width=10)      # sets the input
tk_input.pack()                 # displays on the screen

def change_title_with_input():
    new_text = tk_input.get()
    my_label.config(text=new_text)
    input_button.config(text="Titled changed!")

input_button = Button(text="Change Title", command=change_title_with_input)
input_button.pack()


# print(tk_input.get())


# Starts the Tkinter event loop. This line keeps the window open and responsive to user input.
# It is similar to a 'while True:' loop, continuously listening for events.
# This must be the last line of the script to ensure all widgets are set up before the loop begins.
window.mainloop()
