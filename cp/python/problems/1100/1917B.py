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
    n = int1()
    s = str1()
    feq = {}
    cnt =  0
    dis = [0]*n
    for i in range(n):
        cur = s[i]
        if cur in feq:
            feq[cur] += 1
        else:
            feq[cur] = 1
        if feq[cur] == 1:
            cnt += 1
        dis[i] = cnt
    print(sum(dis))
        
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
