#Function to calculate the steps required to reach 1 using the rules of the Collatz Conjecture.
import sys
def python_version():
    """Function to print the current version of the python its running on.
    
    Parameter:
        Provided the sys library.
    
    Result:
        Outputs the python version its running on.
    
    This function utlizises the sys library to check the version information
    of python and print that to the screen.
    
    """
    
    print(sys.version)

def steps(number):
    """Function to count the steps it takes to reach 1 using the rules of the Collatz Conjecture.
    
    Parameter:
        number (int): provided number on which the rules should be appllied.
        
    Result:
        count (int): The number of steps it takes to reach 1.
        
    This functions uses a while loop to find the number of steps efficiently and faster.
    
    """

    if number < 1:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        count += 1
        if number%2 == 0:
            number //= 2
        else:
            number *= 3
            number += 1
    return count
    
