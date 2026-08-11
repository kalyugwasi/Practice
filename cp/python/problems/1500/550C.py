import sys, os, math
from itertools import combinations
def setup_io():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        judge = os.path.join(base, "..", "judge")
        inpth = os.path.join(judge, "input.txt")
        outpth = os.path.join(judge, "output.txt")
        if os.path.exists(inpth):
            sys.stdin = open(inpth, "r")
            sys.stdout = open(outpth, "w")
            return True
    except:
        pass
    return False

LOCAL = setup_io()
input = sys.stdin.readline
int1 = lambda: int(input())                  # single integer
str1 = lambda: input().strip()                # single stripped string
ints1 = lambda: list(map(int, str1()))        # digits from a string
def inp():  return map(int, input().split())  # multiple ints, unpack: a, b = inp()
def stp():  return map(str, input().split())  # multiple strings
def ints(): return list(map(int, input().split()))  # list of ints
def strs(): return list(map(str, str1()))     # list of chars from a string

# ================= SOLUTION START =================

def solve(p):
    val = int(p)
    if val%8==0:
        print("YES")
        print(val)
        return 1
        
def solver():
    s = str1()
    n = len(s)
    #checking 1 digit:
    for i in range(n):
        if solve(s[i]) == 1:
            return
    #checking 2 digit
    for i in range(n):
        for j in range(i+1,n):
            if solve(s[i]+s[j]) == 1:
                return
    #checking 3 digit
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if solve(s[i]+s[j]+s[k]) == 1:
                    return
    print("NO")

if __name__ == "__main__":
    solver()
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
