def life_in_weeks(age):
    
    weeks_in_a_year = 52
    total_weeks = 90 * weeks_in_a_year          # 4680
    weeks_passed =  age * weeks_in_a_year       # 1300
    weeks_left = total_weeks - weeks_passed
    
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(25)
# You have 3380 weeks left.
