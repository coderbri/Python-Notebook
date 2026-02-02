# 29 Tkinter Password Manager - Changelog

<!-- ## v0.5.0 - Generate a Password & Copy to Clipboard -->

## v0.4.0 - Dialog Boxes and Pop-Ups in Tkinter

- Integrated Tkinter `messagebox` module to provide user feedback.
- Added validation to prevent saving empty website or password fields.
- Implemented an informational pop-up to notify users of input errors.
- Added a confirmation dialog (`askokcancel`) to verify user intent before saving credentials.
- Ensured data is written to file only after explicit user confirmation.
- Improved overall user experience with clearer feedback and safer data handling.

<div align="center">
<img src="./imgs/v0_4_message_popup.png"
    alt="(BETA) Sample `showinfo` message box to show user inputs before confirmation."
    width="200px" height="auto">
</div>

---

## v0.3.0 - Saving Data to File

- Implemented the **Save Data** feature to store user credentials in a local text file.
- Created a `save_data()` function to retrieve input from the website, email, and password fields.
- Appended entries to `data.txt` using the format: `Website | Email/Username | Password`
- Added input-clearing logic after saving for better usability.
- Left a TODO note to add an in-app confirmation message for successful saves.

<div align="center">
<img src="./imgs/v0_3_save_data_to-file.png"
    alt="Window Setup with only the canvas dimensions for the logo."
    width="200px" height="auto">
</div>

---

## v0.2.0 - UI Setup

- Completed the user interface layout using `grid()` instead of `pack()`.
- Implemented a three-column, five-row grid structure for widget alignment.
- Added labels and input fields for **Website**, **Email/Username**, and **Password**.
- Introduced **Generate Password** and **Add** buttons with appropriate positioning.
- Centered the logo at the top using column alignment and improved window spacing for a cleaner layout.

<div align="center">
<img src="./imgs/v0_2_widgets_ui_setup.png"
    alt="Window Setup with only the canvas dimensions for the logo."
    width="200px" height="auto">
</div>

---

## v0.1.0 - Initialize Project

- Created the main application window titled **"Password Manager"**.
- Configured window padding and background color.
- Added a `Canvas` widget with dimensions **200x200px** to display the app logo.
- Loaded and centered the `logo.png` image inside the canvas.
- Finalized basic UI setup as the initial foundation for the project.

<div align="center">
<img src="./imgs/v0_1_password_manager_window_setup.png"
    alt="Window Setup with only the canvas dimensions for the logo."
    width="200px" height="auto">
</div>

---
<section align="center">
  <code>coderBri © 2025</code>
</section>