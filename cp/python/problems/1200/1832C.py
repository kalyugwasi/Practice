import sys,os
from typing import List
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
    a = ints()
    b = [a[0]]
    for i in range(1,n):
        if a[i]!=a[i-1]:
            b.append(a[i])
    if len(b)<=2:
        print(len(b))
        continue
    res = 2
    for i in range(1,len(b)-1):
        if (b[i-1]<b[i]>b[i+1]) or (b[i-1]>b[i]<b[i+1]):
                res += 1
    print(res)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
