# Imported Tkinter classes and math for calculations
from tkinter import *
import math

# ----------------------- CONSTANTS -------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25           # Work session duration (in minutes)
SHORT_BREAK_MIN = 5     # Short break duration (in minutes)
LONG_BREAK_MIN = 20     # Long break duration (in minutes)
reps = 0                # Tracks the number of sessions (work + break)
timer = None            # Global reference to the active timer

# ---------------------- TIMER RESET ------------------------- #
def reset_timer():
    """
    Reset the Pomodoro timer to its initial state:
    - Cancels any active countdown.
    - Resets the timer display to "00:00".
    - Restores the title label to "Timer"
    - Re-initializes the session counter.
    """
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_title_label.config(text="Timer")
    completion_checkmark.config(text="")
    global reps
    reps = 0

# -------------------- TIMER MECHANISM ----------------------- #
def start_timer():
    """
    Start a timer session based on the Pomodoro cycle:
    - Odd reps (1, 3, 4, 7): Work sessions.
    - Even reps (2, 4, 6): Short breaks.
    - Every 8th rep: Long break.
    """
    global reps
    reps += 1   # increment session count each time a new timer starts

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Long break after every 4 work sessions (8th rep total):
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_title_label.config(text="Break", fg=RED)

    # Short break after each work session (2nd, 4th, 6th):
    elif reps % 2 ==0:
        countdown(short_break_sec)
        timer_title_label.config(text="Break", fg=PINK)

    # Work session for 1st, 3rd, 5th, 7th rep
    else:
        countdown(work_sec)
        timer_title_label.config(text="Work", fg=GREEN)

# ------------------ COUNTDOWN MECHANISM --------------------- #
def countdown(count):
    """
    Handle the countdown logic:
    - Updates the timer display each second.
    - Starts the next session when the time reaches zero.
    - Displays a checkmark for every completed work session.
    """
    # Converts total seconds into minutes and seconds
    count_minute = math.floor(count / 60)   # rounds down to the nearest minute
    count_second = count % 60               # remainder seconds after division

    # Format seconds to always show two digits (e.g., "05" instead of "5")
    if count_second < 10:
        count_second = f"0{count_second}"

    # Update timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second}")

    # Continue countdown if time remains
    if count > 0:
        # Schedule the function to run again after 1000ms (1 second)
        global timer # introduce and initialize the variable
        timer = window.after(1000, countdown, count-1)
    else:
        # When countdown finishes, start next timer session automatically
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)   # math.floor rounds the resulting float into an int
        for _ in range(work_sessions):
            """after every, work session, add a completion checkmark"""
            marks += "✔︎"
        completion_checkmark.config(text=marks)

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
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# Timer text overlay
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Start and Reset Buttons
start_btn = Button(
    text="Start", font=(FONT_NAME, 12, "bold"),
    padx=10, pady=5,
    borderwidth=0, highlightthickness=0,
    command=start_timer # 'Start' button triggers countdown
)

reset_btn = Button(
    text="Reset", font=(FONT_NAME, 12, "bold"),
    padx=10, pady=5,
    borderwidth=0, highlightthickness=0,
    command=reset_timer # 'Reset' button triggers reset functionality
)

start_btn.grid(row=2, column=0)
reset_btn.grid(row=2, column=2)

# Completion checkmark.
completion_checkmark = Label(bg=YELLOW, fg=GREEN)
completion_checkmark.grid(row=3, column=1)

window.mainloop()
