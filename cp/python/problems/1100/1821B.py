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
    n,a,b = int1(),ints(),ints()
    l=0
    while l<n and a[l] == b[l]:
        l += 1
    r = n-1
    while r>=0 and a[r] == b[r]:
        r -= 1
    while l>0 and b[l-1] <= b[l]:
        l -= 1
    while r<n-1 and b[r+1] >= b[r]:
        r += 1
    print(l+1,r+1) 
        
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
