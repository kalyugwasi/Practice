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
    a = [0]+ints()
    s,visit = [0]+sorted(a[1:]),[False]*(n+1)
    f = True
    for i in range(1,n+1):
        if not visit[i]:
            ind = []
            j = i
            while j<=n and not visit[j]:
                visit[j] = True
                ind.append(j)
                j *= 2
            if sorted(a[i] for i in ind) != sorted(s[i] for i in ind):
                f = False
                break
    print("YES" if f else "NO")
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
