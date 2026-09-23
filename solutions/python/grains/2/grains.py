# A program to generate the numbers to squares in a chessboard

def square(numbers):
    """Calculates the numbers present at the particular chessboard.

    Parameters:
        numbers (int): The position of the box on the chessboard.

    Result:
        current (int): The value at that exact position on the chessboard

    This function successevely calculates the number upto the desired position on the chessboard.
    
    """
    if numbers <= 0 or numbers > 64:
        raise ValueError("square must be between 1 and 64")
    current = 1
    for _ in range(numbers-1):
        current *= 2
    return current

def total():
    """Calculates the total numbers present upto the final position in the chessboard.
    
    Parameters:
        None : No parameters are required as the final position i.e 64 is already provided.
        
    Result:
        result (int): The value upto the final position the chessboard.
    
    This functions provides the sum of all values till the final position.
    
    """
    current = 1
    result = 1
    for _ in range(63):
        current *=2
        result += current
    return result