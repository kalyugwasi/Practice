#function to determine if the given sides represents a equilateral,isosceles or scalene triangle.

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

def equilateral(sides: list):
    """Function to check if the given sides form the equilateral triangle or not.
    
    Parameters:
        sides (list(a:int,b:int,c:int)): Given sides a,b,c that represents the 3 sides of a triangle.
    
    Output:
        output (bool): A true or false value after checking euality of all sides.
        
    This function checks if the sides are equal or not.
    
    """
    a,b,c = sides
    return a == b and b == c and a > 0 and b > 0 and c > 0
    

def isosceles(sides):
    """Function to check if the given sides form the isoceles triangle or not.
    
    Parameters:
        sides (list(a:int,b:int,c:int)): Given sides a,b,c that represents the 3 sides of a triangle.
    
    Output:
        output (bool): A true or false value after checking two sides are equal or not.
        
    This function checks if two sides are equal or not.
    
    """
    a,b,c = sides
    return (a > 0 and b > 0 and c> 0) and (a+b>=c and b+c>=a and a+c>=b) and (a == b or b == c or a == c)


def scalene(sides):
    """Function to check if the given sides form the scalene triangle or not.
    
    Parameters:
        sides (list(a:int,b:int,c:int)): Given sides a,b,c that represents the 3 sides of a triangle.
    
    Output:
        output (bool): A true or false value after checking all sides are unequal or not.
        
    This function checks if all sides are unequal or not.
    
    """
    a,b,c = sides
    return len(set(sides)) == 3 and (a+b>=c and b+c>=a and a+c>=b) and (a > 0 and b > 0 and c > 0)
