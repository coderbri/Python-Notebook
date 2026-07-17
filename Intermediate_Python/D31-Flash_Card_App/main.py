from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# --------------------------------- UI Setup --------------------------------- #

window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flash Card Canvas
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)

# Display the card language and vocabulary word
canvas.create_text(400, 150, text="French", font=(FONT_NAME, 40, "italic"))
canvas.create_text(400, 263, text="trouve", font=(FONT_NAME, 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Flash card response buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()