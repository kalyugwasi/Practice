import sys,os,math
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
def cs(s,e):
    return ((s+e)*(e-s+1))//2
t = int1()
for _ in range(t):
    n,x,y = inp()
    h = n//((x*y)//math.gcd(x,y))
    c1,c2 = (n//x)-h,(n//y)-h
    res = cs(n-c1+1,n)-cs(1,c2)
    print(res)        
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
