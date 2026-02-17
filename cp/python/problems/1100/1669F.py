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
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================

t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    suf = [0]*n
    im = {}
    s = 0
    for i in range(n-1,-1,-1):
        s += a[i]
        im[s] = i
        suf[i] = s
    pre = 0
    res = 0 
    for i in range(n):
        if suf[i] in im:
            del im[suf[i]]
        pre += a[i]
        if pre in im:
            res = max(res,(i+1)+(n-im[pre]))
    print(res)    
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
