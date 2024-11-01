def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).upper()      # JANE DOEJACK BAUER
    
    # Calculate "TRUE" score
    true_total = 0
    for letter in "TRUE":
        true_total += combined_names.count(letter)
    
    # Calculate "LOVE" score
    love_total = 0
    for letter in "LOVE":
        love_total += combined_names.count(letter)
    
    love_score = str(true_total) + str(love_total)
    print(f"Love Score: {love_score} Points!")


calculate_love_score(name1="Angela Yu", name2="Jack Bauer")
calculate_love_score(name1="Jane Doe", name2="John Smith")
