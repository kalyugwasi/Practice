def square(numbers):
    if numbers <= 0 or numbers > 64:
        raise ValueError("square must be between 1 and 64")
    current = 1
    for i in range(numbers-1):
        current *= 2
    return current

def total():
    current = 1
    total = 1
    for i in range(63):
        current *=2
        total += current
    return total