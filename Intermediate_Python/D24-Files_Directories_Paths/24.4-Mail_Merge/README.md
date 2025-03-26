# 24 Mail Merge 📩  

## Overview  
A Python automation script that generates personalized invitation letters by replacing a placeholder in a template with invitee names.  

## Concepts Implemented  
- File handling (`open()`, `.readlines()`, `.write()`)  
- String manipulation (`.replace()`, `.strip()`)  
- Directory management (`os.path.join()`, `os.makedirs()`)  

## How It Works  
1. Reads names from `invited_names.txt` and stores them in a list.  
2. Reads the `starting_letter.txt` template.  
3. Replaces the `[name]` placeholder with each invitee’s name.  
4. Saves personalized letters in the `Output/ReadyToSend/` folder.  

## Acknowledgments  
Built as part of Dr. Angela Yu’s **100 Days of Code: Python Pro Bootcamp**.  

---

<section align="center">
  <code>coderBri © 2025</code>
</section>