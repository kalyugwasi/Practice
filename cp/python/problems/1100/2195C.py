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
def box(prev,nex):
    for i in range(1,7):
        if i!=prev and i!= m[prev]:
            if nex is None or (i!=nex and i!=m[nex]):
                return i
t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    c = 0
    m = {i:7-i for i in range(1,7)}
    prev = a[0]
    for i in range(1,n):
        if prev == a[i] or a[i] == m[prev]:
            c += 1
            nex = a[i+1] if i+1<n else None
            a[i] = box(prev,nex)
        prev = a[i]
    print(c)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
