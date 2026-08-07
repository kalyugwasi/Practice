import sys, os,math
from collections import Counter
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

def solve(s,l):
    if l == 1 or s=="":
        return True
    ans1 = ans2 = ans3 = False
    if s[:1] == "1": ans1 = solve(s[1:],l-1)
    if s[:2] == "14": ans2 = solve(s[2:],l-2)
    if s[:3] == "144": ans3 = solve(s[3:],l-3)
    return ans1 or ans2 or ans3
n = str1()+" "
print("YES" if solve(n,len(n)) else "NO")



# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py