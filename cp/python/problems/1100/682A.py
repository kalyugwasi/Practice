import sys, os, math
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


n,m = inp()
res = 0
for i in range(1,n+1):
    p = (5-(i%5))%5
    if p == 0: p = 5
    if m >= p: res += 1 + (m-p)//5
    """for j in range(p,m+1,5):
        if j and (i+j)%5 == 0 
            res += 1"""
print(res) 




# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
