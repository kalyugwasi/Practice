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
def inp(): return map(int,input().split())
def ints(): return list(map(int,input().split()))
def strs(): return list(map(str,str1()))
def mint(): return map(int,input().split())
def grid(n): return [ints() for _ in range(n)]
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================

for _ in range(int1()):
    n,k = inp()
    a = ints()
    done = {}
    col = [[]]+[[0] for _ in range(k)]
    col,jumps = [[]],[[]]
    for _ in range(k):
        col.append([0])
        jumps.append([0])
    for i in range(n):
        col[a[i]].append(i+1)
    for i in range(1,k+1):
        col[i].append(n+1)
    res = float("inf")
    for i in range(1,k+1):
        for j in range(len(col[i])-1):
            jl = col[i][j+1]-col[i][j]-1
            heapq.heappush(jumps[i],-jl)
        mv = -heapq.heappop(jumps[i])
        if mv%2 == 0:
            heapq.heappush(jumps[i],-(mv//2))
            heapq.heappush(jumps[i],-((mv//2)-1))
        else:
            heapq.heappush(jumps[i],-(mv//2))
            heapq.heappush(jumps[i],-(mv//2))
        res = min(res,-jumps[i][0])
    print(res)
            
        
    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
