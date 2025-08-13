# Step 28.1: Import all classes in the module.
from tkinter import *

# ----------------------- CONSTANTS -------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------- TIMER RESET ------------------------- #

# -------------------- TIMER MECHANISM ----------------------- #

# ------------------ COUNTDOWN MECHANISM --------------------- #

# ----------------------- UI SETUP --------------------------- #
# Step 28.2: Create main window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Step 28.3: Create Canvas to layer elements (image + text)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load and display tomato image at the center
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Add countdown text over the tomato image
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Place canvas in window
canvas.pack()

window.mainloop()
