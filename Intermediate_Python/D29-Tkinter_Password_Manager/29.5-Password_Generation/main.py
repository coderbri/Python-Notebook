from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WHITE_CLR = "#fff"
BLACK_CLR = "#000"

# ---------------------------- Password Generator ---------------------------- #
def generate_password():
    """
    Generates a secure random password using letters, numbers, and symbols.
    The generated password is inserted into the password entry field and
    automatically copied to the clipboard for improved user experience.
    """
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Randomly determine password composition
    nr_letters = randint(0, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # Build password components
    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    # Combine and shuffle all characters
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # Convert list to string
    password = "".join(password_list)

    # Insert password into entry field and copy to clipboard
    password_input.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")

# ------------------------------ Save Password ------------------------------- #
def save_data():
    """Validates user input, confirms intent, and saves credentials to a file."""
    file_name = "data.txt"

    # Retrieves user input from entry/input fields
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()

    # Validate required fields
    if len(website) == 0 or len(password) == 0:
        # Prevent saving incomplete data
        messagebox.showinfo(
            title="Oops",
            message="Please make sure you haven't left any required fields empty."
        )
    else:
        # Confirm details before saving
        is_ok = messagebox.askokcancel(
            title=website,
            message=(
                f"These are the details entered:\n"
                f"Email: {email_username}\n"
                f"Password: {password}\n\n"
                f"Is it okay to save?"
            )
        )

        # Save data only if user confirms
        if is_ok:
            # Append data to file (creates file if it doesn't exist)
            with open(file_name, "a") as data_file:
                data_file.write(f"{website} | {email_username} | {password}\n")

            print("Data saved!")  # Temporary console confirmation

            # Clear input fields after saving
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
website_input.focus() # Autofocus cursor in this field

email_username_input = Entry(width=35, bg=WHITE_CLR, fg=BLACK_CLR, highlightthickness=0)
email_username_input.insert(0, "janedoe@gmail.com") # Default email text to prepopulate with

password_input = Entry(width=21, bg=WHITE_CLR, fg=BLACK_CLR, highlightthickness=0)

# * Buttons
generate_password_btn = Button(text="Generate Password", width=10,  bg=WHITE_CLR, highlightthickness=0, command=generate_password)
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
