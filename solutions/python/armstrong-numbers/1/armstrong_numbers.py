def is_armstrong_number(number):
    number_as_string = str(number)
    power = len(number_as_string)
    total = sum(int(char) ** power for char in number_as_string)
    return number == total
    

    
