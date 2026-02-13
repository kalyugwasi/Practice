import sys,os,heapq
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
    n,k = inp()
    a = ints()
    a.sort()
    pre = [0]*n
    pre[0] = a[0]
    for i in range(1,n):
        pre[i] += pre[i-1] + a[i]
    mx = 0
    for i in range(k+1):
        s = k-i
        l = 2*i
        r = n-s-1
        sm = pre[r]-(0 if l==0 else pre[l-1])
        mx = max(mx,sm)
    print(mx)
        
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
