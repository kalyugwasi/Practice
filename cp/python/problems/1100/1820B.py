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
int1 = lambda: int(input())
str1 = lambda: input().strip()
ints1 = lambda: list(map(int,str1()))
def inp(): return map(int, input().split())
def ints(): return list(map(int, input().split()))
def strs(): return list(map(str,str1()))
def mint(): return map(int, input().split())
def grid(n): return [ints() for _ in range(n)]
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================

t = int1()
for _ in range(t):
    s = strs()
    n = len(s)
    maxi = 0
    cnt = 0
    for i in range(n):
        if s[i] == "0":
            cnt = 0
        else:
            cnt += 1
        maxi = max(maxi,cnt)
    if maxi == n:
        print(n*n)
        continue
    i = 0
    if s[0] == '1' and s[n-1]== '1':
        cnt = 0
        j = n-1
        while i<n and s[i]== '1':
            i += 1
            cnt += 1
        while j>i and s[j]== '1':
            j -= 1
            cnt += 1
        maxi = max(maxi,cnt)
    maxi += 1
    temp = (maxi+1)//2
    print(temp*(maxi//2))
    
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
