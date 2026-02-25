import sys,os
from itertools import accumulate
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
def bs(i,n):
    p = pmax
    l,h = 0,n-1
    res = -1
    while l<=h:
        mid = (l+h)//2
        if p[mid] <= i:
            res = mid
            l = mid + 1
        else:
            h = mid-1
    return res

t = int1()
for _ in range(t):
    n,q = inp()
    a = ints()
    k = ints()
    res = []
    psum = list(accumulate(a))
    pmax = list(accumulate(a,max))
    for i in k:
        idx = bs(i,n)
        res.append(0 if idx == -1 else psum[idx])
    print(*res)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
