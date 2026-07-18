from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
current_card = {}
words_to_learn = {}

# ------------------------- Vocabulary CSV Extraction ------------------------ #
try:
    # Attempt to load progress from a previous session
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Fallback ot the full vocabulary list if no progress file exists
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


# --------------------------------- Next Card -------------------------------- #
def next_card():
    """Selects a new random card and resets the 3-second flip timer."""
    global current_card, flip_timer
    window.after_cancel(flip_timer) # Stop existing timer if user clicks early
    current_card = random.choice(words_to_learn)

    # UI for French Vocabulary
    canvas.itemconfig(language_title_text, text="French", fill="black")
    canvas.itemconfig(vocab_word_text, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)

    # Star new 3-second countdown
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    """Flips the card to show the English translation."""
    canvas.itemconfig(language_title_text, text="English", fill="white")
    canvas.itemconfig(vocab_word_text, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    """Removes the current card from the deck and saves remaining progress to CSV."""
    words_to_learn.remove(current_card)

    # Update progress file: index=False prevents pandas from adding redundant row numbers
    unlearned_words = pandas.DataFrame(words_to_learn)
    unlearned_words.to_csv("data/words_to_learn.csv", index=False)

    next_card()

# --------------------------------- UI Setup --------------------------------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card) # --> set 3s (3000ms) delay

# Flash Card Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)

# Display Text Elements
language_title_text = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
vocab_word_text = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

next_card() # Initialize app state with random card
window.mainloop()