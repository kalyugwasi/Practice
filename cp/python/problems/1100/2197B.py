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
    p = ints()
    res = [float("inf")]*n
    a = ints()
    for i in range(n-1,-1,-1):
        if p[i] == a[i]:
            res[i] = p[i]
            continue
        l = r = False
        if i+1<n and (p[i+1]==a[i] or res[i+1]==a[i]):
            l = True
        if i-1>=0 and p[i-1]==a[i]:
            r = True
        if l or r:
            res[i] = a[i]
        else:
            break
    if res == a:
        print("YES")
    else:
        print("NO")
            
        
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
