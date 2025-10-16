from tkinter import *

WHITE_CLR = "#fff"
BLACK_CLR = "#000"

# ---------------------------- Password Generator ---------------------------- #
# (Features to be implemented later)

# ------------------------------ Save Password ------------------------------- #
# (Features to be implemented later)

# --------------------------------- UI Setup --------------------------------- #
# Main application window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE_CLR)

# Canvas to display the logo at the center
canvas = Canvas(height=200, width=200, bg=WHITE_CLR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# ! not needed anymore -> canvas.pack()
canvas.grid(row=0, column=1)

# ------------------------------- UI Components ------------------------------ #
# * Labels
website_text_label = Label(text="Website:", bg=WHITE_CLR, fg=BLACK_CLR)
email_username_text_label = Label(text="Email/Username:", bg=WHITE_CLR, fg=BLACK_CLR)
password_text_label = Label(text="Password:", bg=WHITE_CLR, fg=BLACK_CLR)

# * Entry Fields
website_input = Entry(width=35, bg=WHITE_CLR, highlightthickness=0,)
email_username_input = Entry(width=35, bg=WHITE_CLR, highlightthickness=0,)
password_input = Entry(width=21, bg=WHITE_CLR, highlightthickness=0,)

# * Buttons
generate_password_btn = Button(text="Generate Password", width=10,  bg=WHITE_CLR, highlightthickness=0)
add_btn = Button(text="Add", width=32, bg="blue")

# ------------------------------- Grid Placement ----------------------------- #
website_text_label.grid(row=1, column=0)
email_username_text_label.grid(row=2, column=0)
password_text_label.grid(row=3, column=0)

website_input.grid(row=1, column=1, columnspan=2, pady=5)
email_username_input.grid(row=2, column=1, columnspan=2, pady=5)
password_input.grid(row=3, column=1, pady=5)

generate_password_btn.grid(row=3, column=2, pady=5)
add_btn.grid(row=4, column=1, columnspan=2)

# Keep the window open and responsive
window.mainloop()
