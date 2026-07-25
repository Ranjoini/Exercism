"""Functions to confirm if the year given was a leap year"""
def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True 
    return False
