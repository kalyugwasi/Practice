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

p = []
h = 1
while True:
    cards = (3*h*h+h)//2
    if cards > 10**9:
        break
    p.append(cards)
    h += 1

for i in range(int1()):
    n = int1()
    ans = 0
    while n >= 2:
        idx = br(p,n) - 1
        if idx < 0:
            break
        n -= p[idx]
        ans += 1
    print(ans)    
    
    
    
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
