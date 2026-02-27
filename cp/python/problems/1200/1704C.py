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
def inp(): return map(int,input().split())
def ints(): return list(map(int,input().split()))
def strs(): return list(map(str,str1()))
def mint(): return map(int,input().split())
def grid(n): return [ints() for _ in range(n)]
def grids(n): return [ints1() for _ in range(n)]
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================

t = int1()
for _ in range(t):
    n,m = inp()
    a = sorted(ints())
    gaps = []
    for i in range(m-1):
        gaps.append(a[i+1]-a[i]-1)
    gaps.append(a[0]+n-a[-1]-1)
    nd,ns = 0,0
    for i in sorted(gaps,reverse=True):
        cur = i - nd * 2
        if cur>0:
            ns += 1
            cur -= 2
            if cur>0 :
                ns += cur
            nd += 2
    print(n-ns)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
