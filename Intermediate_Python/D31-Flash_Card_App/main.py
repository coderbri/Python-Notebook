from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# ------------------------- Vocabulary CSV Extraction ------------------------ #
data = pandas.read_csv("data/french_words.csv")
# Convert to list of dicts for easy access: [{'French': 'English': translation}, ...]
vocab_to_learn = data.to_dict(orient="records")

# --------------------------------- Next Card -------------------------------- #
def next_card():
    """Picks a random word from the dataset and updates the canvas display."""
    current_card = random.choice(vocab_to_learn)
    canvas.itemconfig(language_title, text="French", fill="black")
    canvas.itemconfig(vocab_word, text=current_card["French"], fill="black")

# --------------------------------- UI Setup --------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

# Display the card language and vocabulary word
language_title = canvas.create_text(400, 150, text="", font=(FONT_NAME, 40, "italic"))
vocab_word = canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Flash card response buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card() # Ensures a new card is always up after all components are rendered

window.mainloop()