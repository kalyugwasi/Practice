#Function to check if the number is armstrong or not.

def is_armstrong_number(number):
    """Calculates and check if the number provided is armstrong number or not.
    
    Parameters:
        number (int): The number that should be checked against the conditions.
    
    Result:
        result (Bool): True if number is armstrong else False
    
    It check the code for the following conditions:
    1. If n is the provided number then n == n^1 == n
    2. If nml in the provided number then nml = n^3 + m^3 + l^3 = nml 
    """
    number_in_str = str(number)
    length = len(number_in_str)
    result = 0
    for num in number_in_str:
        result += int(num)**length
    return result == number if length > 1 else True
