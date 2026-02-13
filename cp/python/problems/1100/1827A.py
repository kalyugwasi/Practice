import sys,os,bisect
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
MOD = 10**9 + 7
t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    b = ints()
    a.sort()
    b.sort(reverse=True)
    res = 1
    for i in range(n):
        res = res * max(n-bisect.bisect_right(a,b[i])-i,0)%MOD
    print(res)
    



# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
