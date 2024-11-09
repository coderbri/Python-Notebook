def is_leap_year(year):
    
    if year % 4 == 0:
        # 'True' so far,  so keep checking
        if year % 100 == 0:
            # if still 'True',  so keep checking
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

print(is_leap_year(2400))   # True
print(is_leap_year(1989))   # False
print(is_leap_year(2100))   # False