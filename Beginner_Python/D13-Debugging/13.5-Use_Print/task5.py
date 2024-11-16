# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)      # ? Currently ouputing 0

# * Debugged Code

word_per_page = 0
pages = int(input("Number of pages: "))
print(f"Pages: {pages}")

word_per_page = int(input("Number of words per page: "))
print(f"Words per page: {word_per_page}")

total_words = pages * word_per_page
print(f"Total Words: {total_words}")

# SAMPLE OUTPUT
# Number of pages: 30
# Pages: 30
# Number of words per page: 900
# Words per page: 900
# Total Words: 27000
