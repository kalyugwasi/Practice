import sys,os
from bisect import bisect_left
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
    n = int1()
    a = [(v,i) for i,v in enumerate(ints())]
    a.sort()
    res = [0]*n
    pre = res.copy()
    pre[0] = a[0][0]
    for i in range(1,n):
        pre[i] = pre[i-1]+a[i][0]
    for i in range(n):
        j = i
        found = i
        while j<n:
            temp = (pre[j]+1,float('-inf'))
            idx = bisect_left(a,temp)
            idx -= 1
            if idx == j:
                break
            found +=idx-j
            j = idx
        res[a[i][1]]= found
    print(*res)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
