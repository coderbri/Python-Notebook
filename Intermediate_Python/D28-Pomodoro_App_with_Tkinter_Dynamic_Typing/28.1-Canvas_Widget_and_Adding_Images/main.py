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
# Create main window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Step 28.1.1: Timer title setup.
timer_title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_title_label.grid(row=0, column=1)

# Create Canvas to layer elements (image + text)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load and display tomato image and timer at the center
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Step 28.1.2: Start and Reset buttons (styling only, no functionality yet)
start_btn = Button(
    text="Start", font=(FONT_NAME, 12, "bold"),
    padx=10, pady=5,
    borderwidth=0, highlightthickness=0
)

reset_btn = Button(
    text="Reset", font=(FONT_NAME, 12, "bold"),
    padx=10, pady=5,
    borderwidth=0, highlightthickness=0
)

start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

# Step 28.1.3: Completion checkmark.
completion_checkmark = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
completion_checkmark.grid(row=3, column=1)

window.mainloop()
