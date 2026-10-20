"""Module providing a function printing python version."""
import sys
def print_python_version():
    print(sys.version)

def convert(number):
    '''
    A function to return a string based on the divisibility of the input
    
    Parameters:
        number (int): provided input to test against
    Output:
        result (string): resulting output based on the divisibility
    
    Working:
    1. If number is disivible by 3 add "Pling" to the result
    2. If number is divisible by 5 add "Plang" to the result
    3. If number is divisible by 7 add "Plong" to the result
    4. A number can be divisible by one or many
    5. If it is not visible by anything the number should return itself in form of a string
    '''
    
    result = ""
    if number%3 == 0: result += "Pling"
    if number%5 == 0: result += "Plang"
    if number%7 == 0: result += "Plong"
    if result == "":
        return f"{number}"
    return result