#function to calculate if the given year is a leap year or not.

"""Module providing a function printing python version."""
import sys


def print_python_version():
    """Function to print the current version of the python its running on.
    
    Parameter:
        Provided the sys library.
    
    Result:
        Outputs the python version its running on.
    
    This function utlizises the sys library to check the version information
    of python and print that to the screen.
    
    """
    print(sys.version)


def leap_year(year):
    """Calculates if the given year is a leap year or not.
    
    Parameter:
        year (int): Provided year in int form.
    
    Result:
        result (bool): Boolean True or False depending upon the answer.
        
    This function checks the provided year if it is a leap year or not.
    """

    result = False
    if year%4==0 and year%100!=0 or (year%400==0):
        result = True
    return result