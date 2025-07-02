#!/usr/bin/env python3
"""
Odd Even Divisors Problem

For any number N = 2^k * m where m is odd:
- Odd divisors of N are exactly the divisors of m
- Even divisors of N are obtained by multiplying each odd divisor by powers of 2 (2^1 to 2^k)
- If A = number of odd divisors and B = number of even divisors, then B = A * k

Solution logic:
- If A = 0: No number has 0 odd divisors (impossible)
- If B = 0: Number must be odd (possible for any A > 0)
- If A > 0 and B > 0: B must be divisible by A for a solution to exist
"""

def solve_odd_even_divisors():
    """
    Solve the Odd Even Divisors problem for multiple test cases.
    
    Input:
    - First line: T (number of test cases)
    - For each test case: two integers A and B
    
    Output:
    - "Yes" if a number exists with exactly A odd divisors and B even divisors
    - "No" otherwise
    """
    t = int(input())
    
    for _ in range(t):
        a, b = map(int, input().split())
        
        # Case 1: A = 0 means no odd divisors, which is impossible
        # Every number has at least 1 as an odd divisor
        if a == 0:
            print("No")
            continue
        
        # Case 2: B = 0 means no even divisors
        # This happens when the number is odd, which is always possible
        if b == 0:
            print("Yes")
            continue
        
        # Case 3: Both A > 0 and B > 0
        # For N = 2^k * m (m odd), we have B = A * k
        # So B must be divisible by A
        if b % a == 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve_odd_even_divisors()