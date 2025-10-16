from tkinter import *

WHITE_CLR = "#fff"
BLACK_CLR = "#000"

# ---------------------------- Password Generator ---------------------------- #
# (Features to be implemented later)

# ------------------------------ Save Password ------------------------------- #
def save_data():
    """Retrieves user input and stores website, email, and password data in a file"""
    file_name = "data.txt"

    # Collect input data from the entry fields
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    # Append data to file (creates file if it doesn't exist)
    with open(file_name, "a") as data_file:
        data_file.write(f"{website} | {email_username} | {password}\n")

    print("Data saved!") # Temporary confirmation in console
    # TODO: Display confirmation message in the UI

    # Clear website and password fields after saving
    website_input.delete(0, END)
    password_input.delete(0, END)

# --------------------------------- UI Setup --------------------------------- #
# Main application window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE_CLR)

# Canvas to display the logo at the center
canvas = Canvas(height=200, width=200, bg=WHITE_CLR, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ------------------------------- UI Components ------------------------------ #
# * Labels
website_text_label = Label(text="Website:", bg=WHITE_CLR, fg=BLACK_CLR)
email_username_text_label = Label(text="Email/Username:", bg=WHITE_CLR, fg=BLACK_CLR)
password_text_label = Label(text="Password:", bg=WHITE_CLR, fg=BLACK_CLR)

# * Entry Fields
website_input = Entry(width=35, bg=WHITE_CLR, fg=BLACK_CLR, highlightthickness=0)
website_input.focus() # Auto-focus cursor in this field

email_username_input = Entry(width=35, bg=WHITE_CLR, fg=BLACK_CLR, highlightthickness=0)
email_username_input.insert(0, "janedoe@mail.com") # Default email text

password_input = Entry(width=21, bg=WHITE_CLR, fg=BLACK_CLR, highlightthickness=0)

# * Buttons
generate_password_btn = Button(text="Generate Password", width=10,  bg=WHITE_CLR, highlightthickness=0)
add_btn = Button(text="Add", width=32, command=save_data)

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
