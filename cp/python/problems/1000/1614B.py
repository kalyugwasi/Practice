import sys,os
from collections import deque
def setup_io():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        judge = os.path.join(base,"..","judge")
        inpth = os.path.join(judge,"input.txt")
        outpth = os.path.join(judge,"output.txt")
        if os.path.exists(inpth):
            sys.stdin = open(inpth,"r")
            sys.stdout = open(outpth,"w")
            return True
    except:
        pass
    return False
LOCAL = setup_io()
input = sys.stdin.readline
int1 = lambda: int(input()) #for reading a single number
str1 = lambda: input().strip() #for spliting a char in parts
ints1 = lambda: list(map(int,str1())) #mostly for 0,1
def inp(): return map(int, input().split()) #mainly for multiple known variables
def ints(): return list(map(int, input().split())) #for numerical lists
def strs(): return list(map(str,str1())) #for string list

# ================== SOLUTION START =================

t = int1()
for _ in range(t):
    n = int1()
    a = [(val,key) for key,val in enumerate(ints())]
    a.sort(reverse=True,key=lambda x:x[0])
    res = [0]*(n+1)
    sol,cord = 0,1
    for i in range(n):
        res[a[i][1]+1] = cord
        sol += (2*abs(cord)*a[i][0])
        if cord < 0:
            cord = abs(cord) + 1
        else:
            cord = -cord
    print(sol)
    print(*res)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
#cfjudge
#python run.py