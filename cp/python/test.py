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
n = t*(t+1)//2
if n%2!=0:
    print("NO")
else:
    print("YES")
    set1,set2=[],[]
    if t%4==0:
        for i in range(1,t+1,4):
            set1.append(i)
            set1.append(i+3)
            set2.append(i+1)
            set2.append(i+2)
    else:
        set1.extend([1,2])
        set2.append(3)
        for i in range(4,t+1,4):
            set1.append(i)
            set1.append(i+3)
            set2.append(i+1)
            set2.append(i+2)
    print(len(set1))
    print(*set1)
    print(len(set2))
    print(*set2)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
