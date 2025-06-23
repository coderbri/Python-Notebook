from tkinter import *
# It's recommended to use 'from tkinter import *' for convenience in learning.
# For larger applications, it's often better to import specific modules (e.g., 'import tkinter as tk')
# to avoid name clashes and make the code's origin clearer.

# * Button Creation & Functionality
def button_clicked():
    new_text = "I got clicked"
    button2.config(text=new_text) # Changes the button's text after it's clicked
    print(new_text)

# Window Screen Setup
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Add space/padding around the window's content
window.config(padx=100, pady=200)

# Label Creation
my_label = Label(text="I am a label", font=("Courier", 16, "bold"))
my_label.config(text="LABEL")
# my_label.pack() # Example of .pack() - currently commented out

# * Label with .pack(side)
label2 = Label(text="Using .pack(side)", font=("Courier", 16, "bold"))
# label2.pack(side="left") # Example of .pack(side) - currently commented out

# * Button with .place(x, y)
# button = Button(text="Using .place(x=100, y=200)", command=button_clicked)
# button.place(x=100, y=200) # Example of .place() - currently commented out

# * Entry Component: an input field
# * Input with .grid(column, row) - active layout manager in this code
tk_input = Entry(width=20)
tk_input.insert(END, string="Using .grid(column, row)")
# tk_input.grid(column=2, row=2) # Example of .grid() for an Entry - currently commented out

# Widgets using the grid layout manager:
my_label.grid(column=0, row=0) # Places my_label in the first column, first row

button2 = Button(text="Button", command=button_clicked)
button2.grid(column=2, row=1) # Places button2 in the third column, second row

button3 = Button(text="New Button", command=button_clicked)
button3.grid(column=3, row=0) # Places button3 in the fourth column, first row

entry_input = Entry(width=10)
entry_input.insert(END, string="Entry Input")
entry_input.grid(column=4, row=3) # Places entry_input in the fifth column, fourth row

# Starts the Tkinter event loop. This line keeps the window open and responsive to user input.
# It is similar to a 'while True:' loop, continuously listening for events.
# This must be the last line of the script to ensure all widgets are set up before the loop begins.
window.mainloop()