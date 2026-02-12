import sys,os
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
    n,k,a,b = inp()
    x = [0]*(n+1)
    y = [0]*(n+1)
    ma = mb = float("inf")
    for i in range(1,n+1):
        x[i],y[i] = inp()
    res = abs(x[a]-x[b])+abs(y[a]-y[b])
    for i in range(1,k+1):
        ma = min(ma,abs(x[a]-x[i])+abs(y[a]-y[i]))
        mb = min(mb,abs(x[b]-x[i])+abs(y[b]-y[i]))
    print(min(res,ma+mb))


# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
