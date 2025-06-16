from tkinter import *
# recommended to use it this way if many classes are used as in this learning case.
# however, if there's only a few classes, only the module need to imported

# Window Screen Setup
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=700)

# Label Creation
my_label = Label(text="The quick brown fox jumps over the lazy dog.",
                         font=("Courier", 16, "bold"))
my_label.pack() # to make it appear in the screen


# Two ways to change text in a label
my_label["text"] = "New text"
my_label.config(text="This is New Text")

# Button Creation & Functionality
def button_clicked():
    new_text="I got clicked"
    button.config(text=new_text) # Changes the button's text after it's clicked
    print(new_text)

button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry Component
tk_input = Entry(width=10)  # Sets the input field with a width of 10 characters
tk_input.pack()             # Displays the input field on the screen

def change_title_with_input():
    new_text = tk_input.get()                   # Get the text currently in the Entry widget
    my_label.config(text=new_text)              # Update the my_label text with the input
    input_button.config(text="Titled changed!") # Change the button's text

input_button = Button(text="Change Title", command=change_title_with_input)
input_button.pack()

# * MORE TKINTER WIDGETS
# * Another Entry Box Example
entry_label = Label(text="Entry Box", font=("Courier", 12, "bold"))
entry_label.pack()

entry_box = Entry(width=30)
entry_box.insert(END, string="Some text to begin with...")  # adds some text to begin with
print(entry_box.get())  # prints to console the inserted text from above
entry_box.pack()

# * Text Entry Box: allows users to write multiple lines of text
textbox_label = Label(text="Text Entry Box", font=("Courier", 12, "bold"))
textbox_label.pack()

textbox = Text(height=5, width=30)
textbox.focus()    # adds a cursor in textbox
textbox.insert(END, "Example of multi-line text entry...")
print(textbox.get("1.0", END)) # gets current value in textbox at line 1, character 0
textbox.pack()

# * Spinbox: a sort of counter you can go up and down
spinbox_label = Label(text="Spinbox", font=("Courier", 12, "bold"))
spinbox_label.pack()

def spinbox_used():
    """gets current value in spinbox"""
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# * Scale: a slider that users can move along its axis and change its value
scale_label = Label(text="Scale", font=("Courier", 12, "bold"))
scale_label.pack()

def scale_used(value):
    """call the current scale value"""
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# * Checkbox, Radio Buttons: a tick box or anything that can be switched on and off
checkbox_label = Label(text="Checkbox", font=("Courier", 12, "bold"))
checkbox_label.pack()

def checkbox_used():
    """prints 1 if On button checked, otherwise 0."""
    print(checked_state.get())
checked_state = IntVar() # an object created form from a class to track the value of a checkbox
check_button = Checkbutton(text="Is On?", variable=checked_state, command=checkbox_used)
checked_state.get()
check_button.pack()

radiobutton_label = Label(text="Radio Buttons", font=("Courier", 12, "bold"))
radiobutton_label.pack()

def radio_used():
    print(radio_state.get())
# variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# * Listbox: a list of choices to pick from; a multiselect
listbox_label = Label(text="Listbox", font=("Courier", 12, "bold"))
listbox_label.pack()

def listbox_used(event):
    """gets current selection form listbox"""
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Mango", "Cherry"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


# Starts the Tkinter event loop. This line keeps the window open and responsive to user input.
# It is similar to a 'while True:' loop, continuously listening for events.
# This must be the last line of the script to ensure all widgets are set up before the loop begins.
window.mainloop()
