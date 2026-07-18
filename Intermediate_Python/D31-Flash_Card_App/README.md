# Flash Card App - Capstone Project

## 31.2 • Data Integration & Card Logic
**Release Date:** July 17, 2026

- **Implemented Pandas Data Extraction:** Integrated `pandas` to read the `french_words.csv` file. 
- **Optimized Data Formatting:** Converted raw CSV data into a list of dictionaries using `data.to_dict(orient="records")`. This approach improves data accessibility compared to the default `to_dict()` behavior:
    - **Default (Nested):** Creates a column-centric structure: `{'French': {0: 'partie', 1: 'histoire'}, 'English': {0: 'part', 1: 'history'}}`. This requires complex indexing to access specific word pairs.
    - **`orient="records"` (Flat):** Creates an iterable list of row-centric dictionaries: `[{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]`. This allows for direct key-based access (e.g., `current_card["French"]`).
- **Added `next_card()` Functionality:** Created core logic to randomly select a dictionary entry from the vocabulary list using `random.choice()`.
- **Dynamic UI Updates:** Configured the `next_card()` function to update the canvas text elements (`language_title` and `vocab_word`) with the selected French vocabulary.
- **Event Binding:** Linked both the "Known" and "Unknown" buttons to the `next_card()` function to trigger a fresh word selection upon every click.

---

## 31.1 • Creating the UI
**Release Date:** July 17, 2026

- Created the main Tkinter application window.
- Configured window padding and background color.
- Added image assets for the flash card and response buttons.
- Created the flash card canvas and displayed the front card image.
- Added placeholder text for the language and vocabulary word.
- Created "Known" and "Unknown" response buttons with image icons.
- Added a CSV file containing French words and their English translations.
- Organized the initial user interface using Tkinter's grid layout.

---
<section align="center">
  <code>coderBri © 2026</code>
</section>