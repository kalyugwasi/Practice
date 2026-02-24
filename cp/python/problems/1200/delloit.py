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
    a = grid(n)
    cities = {i:[] for i in range(n)}
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                cities[i].append(j)
    def dfs(u,r,seen):
        seen[u] = True
        for v in cities[u]:
            if v == r:
                continue
            if not seen[v]:
                dfs(v,r,seen)
    res = []
    for r in range(n):
        seen = [False] * n
        start = -1
        for i in range(n):
            if i!=r:
                start = i
                break
        if start == -1:
            continue
        dfs(start,r,seen)
        cnt = 0
        for i in range(n):
            if i!=r and seen[i]:
                cnt += 1
        if cnt != n-1:res.append(r)
    print(*res if res else -1)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
