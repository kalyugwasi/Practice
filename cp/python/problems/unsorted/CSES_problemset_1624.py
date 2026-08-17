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

board = [str1() for _ in range(8)]
col = set();hy = set();hx = set()
res = 0 
def btrack(r):
    if r == 8:
        global res
        res += 1
        return
    for c in range(8):
        if c in col or (board[r][c] == "*") or (r+c) in hy or (r-c) in hx:
            continue

        col.add(c)
        hy.add(r+c)
        hx.add(r-c)

        btrack(r+1)

        col.remove(c)
        hy.remove(r+c)
        hx.remove(r-c)
btrack(0) 
print(res)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()