#!/usr/bin/env python3
import sys, os, math
from collections import Counter
from bisect import bisect_right as br
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

n = 7
st = strs()
res = 0
sys.setrecursionlimit(1000)
visited = 0
def blocked(r, c, visited):
    if r < 0 or r >= 7 or c < 0 or c >= 7:
        return True
    cell = r*7+c
    return visited & (1<<cell)
def dfs(i,r,c,visited):
    if blocked(r,c, visited):
        return
    if (r,c) == (6,0): 
        if i == 48:
            global res
            res += 1
        return
    cell = r*7+c
    visited |= (1<<cell)
    if (blocked(r, c-1, visited)
        and blocked(r, c+1, visited)
        and not blocked(r-1, c, visited)
        and not blocked(r+1, c, visited)):
        return
    if (blocked(r-1, c, visited)
        and blocked(r+1, c, visited)
        and not blocked(r, c-1, visited)
        and not blocked(r, c+1, visited)):
        return
    if st[i] == "?":
        dfs(i+1,r+1,c, visited)
        dfs(i+1,r,c+1, visited)
        dfs(i+1,r-1,c, visited)
        dfs(i+1,r,c-1, visited)
    elif st[i] == 'R': dfs(i+1,r,c+1,visited)
    elif st[i] == 'U': dfs(i+1,r-1,c,visited)
    elif st[i] == 'D': dfs(i+1,r+1,c,visited)
    else: dfs(i+1,r,c-1,visited)
    visited ^= 1<<cell
dfs(0,0,0,0)
print(res)







# ================== SOLUTION END ==================
if LOCAL:
    sys.stdout.flush()