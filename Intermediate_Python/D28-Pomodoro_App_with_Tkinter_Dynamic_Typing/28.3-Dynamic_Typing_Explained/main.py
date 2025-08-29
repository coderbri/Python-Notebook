# Imported Tkinter classes and math for calculations
from tkinter import *
import math

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
def start_timer():
    """Start the timer by triggering the countdown."""
    # Currently hardcoded to 5 minutes (5 * 60 seconds).
    countdown(5 * 60) # ? W/o dynamic typing, alone will display 300s

# ------------------ COUNTDOWN MECHANISM --------------------- #
def countdown(count):
    """Update the timer display every second until the countdown reaches 0."""

    # Converts total seconds into minutes and seconds
    count_minute = math.floor(count / 60)   # rounds down to the nearest minute
    count_second = count % 60               # remainder seconds after division

    # NEW! * Ensures seconds are always displayed with two digits (e.g., 05 instead of 5)
    if count_second < 10:
        count_second = f"0{count_second}"

    # Update the canvas text with the formatted time
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")

    # Continue countdown if time remains
    if count > 0:
        # Schedule the function to run again after 1000ms (1 second)
        window.after(1000, countdown, count-1)

# ----------------------- UI SETUP --------------------------- #
# Create main window
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Display 'Timer' label
timer_title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), bg=YELLOW, fg=GREEN)
timer_title_label.grid(row=0, column=1)

# Create Canvas to layer elements (image + text)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Load and display tomato image and timer at the center
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start and Reset Buttons
start_btn = Button(
    text="Start", font=(FONT_NAME, 12, "bold"),
    padx=10, pady=5,
    borderwidth=0, highlightthickness=0,
    command=start_timer # ? 'Start' button triggers countdown
)

reset_btn = Button(
    text="Reset", font=(FONT_NAME, 12, "bold"),
    padx=10, pady=5,
    borderwidth=0, highlightthickness=0
)

start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

# Completion checkmark.
completion_checkmark = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
completion_checkmark.grid(row=3, column=1)

window.mainloop()
