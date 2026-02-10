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

# ================= SOLUTION START =================

t = int1()
for _ in range(t):
    n,k = inp()
    a = ints()
    b = ints()
    exp = 0
    mx,s = 0,0
    for i in range(min(n,k)):
        s += a[i]
        mx = max(mx,b[i])
        exp = max(exp,s+(k-(i+1))*mx)
    print(exp)
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
