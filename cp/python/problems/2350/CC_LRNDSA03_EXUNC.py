#!/usr/bin/env python3
import sys, os
def setup_io():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        judge = os.path.join(base, "..", "judge")
        inpth = os.path.join(judge, "input.txt")
        outpth = os.path.join(judge, "output.txt")
        if os.path.exists(inpth):
            sys.stdin = open(inpth, "r")
            sys.stdout = open(outpth, "w")
            return True
    except:
        pass
    return False

LOCAL = setup_io()
input = sys.stdin.readline
int1 = lambda: int(input())                  # single integer
str1 = lambda: input().strip()                # single stripped string
ints1 = lambda: list(map(int, str1()))        # digits from a string
def inp():  return map(int, input().split())  # multiple ints, unpack: a, b = inp()
def stp():  return map(str, input().split())  # multiple strings
def ints(): return list(map(int, input().split()))  # list of for _ in range(int1()):
def strs(): return list(map(str, str1()))     # list of chars from a string
#print = sys.stdout.write

# ================= SOLUTION START =================
from bisect import bisect_right as br
n,q = inp()
a = ints()
start = [0]
for i in range(1,n):
    if a[i]%a[i-1]!=0:
        start.append(i)
for _ in range(q):
    val = ints()
    if val[0] == 1:
        idx = val[1]-1
        a[idx] = val[2]
        if idx>0:
            cond = (a[idx]%a[idx-1] != 0)
            p = br(start, idx) - 1
            is_start = (start[p] == idx)
            if cond and not is_start:
                start.insert(p + 1, idx)
            elif not cond and is_start:
                start.pop(p)
        if idx + 1 < n:
            cond = (a[idx + 1] % a[idx] != 0)
            p = br(start, idx + 1) - 1
            is_start = (start[p] == idx + 1)
            if cond and not is_start:
                start.insert(p + 1, idx + 1)
            elif not cond and is_start:
                start.pop(p)
    else:
        idx = val[1]-1
        p = br(start,idx)-1
        print(start[p]+1)

"""
chain = []
def cha():
    chain = [[0,0]]
    for r in range(1,n):
        if a[r]%a[r-1]==0:
            chain[-1][1] = r
            continue
        chain.append([r,r])
    return chain
n,q = inp()
a = ints()
for i in range(q):
    val = ints()
    if len(val) == 3:
        a[val[1]-1] = val[2]
        chain = cha()
    else:
        for s,e in chain:
            if val[1] in range(s+1,e+2):
                print(s+1)
"""


# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
