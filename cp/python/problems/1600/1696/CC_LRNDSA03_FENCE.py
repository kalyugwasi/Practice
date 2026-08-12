#!/usr/bin/env python3
import sys, os, math
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
def ints(): return list(map(int, input().split()))  # list offor _ in range(int1()):
def strs(): return list(map(str, str1()))     # list of chars from a string
#print = sys.stdout.write

# ================= SOLUTION START =================

"""for _ in range(int1()):
    n,m,k = inp()
    grid = [["."]*m for i in range(n)]
    for i in range(k):
        r,c = inp()
        grid[r-1][c-1] = "x"
    seen  = []
    def solve(r,c):
        if (r,c) in seen: return 0
        if r < 0 or r >= n or c<0 or c>=m or grid[r][c] == ".":
            return 1
        res = 0
        seen.append((r,c))
        res = solve(r-1,c) + solve(r,c-1) + solve(r+1,c) + solve(r,c+1)
        return res
    out = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "x" and (i,j) not in seen: 
                out += solve(i,j)
    print(out)
"""
for _ in range(int1()):
    n,m,k = inp()
    plants = set()
    for _ in range(k):
        r,c = inp()
        plants.add((r,c))
    res = 0
    dire = [(-1,0),(0,-1),(1,0),(0,1)]
    for r,c in plants:
        f = 4
        for dr,dc in dire:
            if (r+dr,c+dc) in plants:
                f -= 1
        res += f
    print(res)
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
