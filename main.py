def check_odd_even(number):
    
    if not isinstance(number, int):
        return "Invalid Input: Not an Integer"
    
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"