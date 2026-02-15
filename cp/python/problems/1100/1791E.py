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
    n = int1()
    a,b = [0],[]
    for i in sorted(ints()):
        if i<1:
            b.append(-i)
        else:
            a.append(i+a[-1])
    res = a[-1]+sum(b)
    p = len(b)
    if p%2!=0:
        h = b[-1]
        if len(a)>1:
            res -= h*2 if a[1]>h else a[1]*2
        else:
            res -= h*2
    print(res)
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
