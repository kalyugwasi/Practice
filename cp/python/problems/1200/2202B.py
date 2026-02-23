import sys,os
from functools import lru_cache
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
def inp(): return map(int,input().split())
def ints(): return list(map(int,input().split()))
def strs(): return list(map(str,str1()))
def mint(): return map(int,input().split())
def grid(n): return [ints() for _ in range(n)]
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================
def dfs(l,r,i):
    if i==n:return True
    if l>r:return False
    lc,rc = "a" if l%2==0 else "b","a" if r%2==0 else "b"
    c = x[i]
    if c =="?":
        return dfs(l+1,r,i+1) or dfs(l,r-1,i+1)
    res = False
    if c == lc:
        res |= dfs(l+1,r,i+1)
    if c == rc:
        res |= dfs(l,r-1,i+1)
    return res
t = int1()
for _ in range(t):
    n = int1()
    x = str1()
    print("YES" if dfs(0,n-1,0) else "NO")   

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
