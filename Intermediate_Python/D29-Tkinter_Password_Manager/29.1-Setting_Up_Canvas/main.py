from tkinter import *

# ---------------------------- Password Generator ---------------------------- #
# (Features to be implemented later)

# ------------------------------ Save Password ------------------------------- #
# (Features to be implemented later)

# --------------------------------- UI Setup --------------------------------- #
# Create the main application window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="#fff")

# Add a canvas to display the logo at the center
canvas = Canvas(height=200, width=200, bg="#fff", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

# Keep the window open and responsive
window.mainloop()
