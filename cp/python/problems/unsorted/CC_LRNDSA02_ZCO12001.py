#!/usr/bin/env python3
import sys, os, math
from collections import Counter
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


n = int1()
a = ints()
nd = fnd = mlm = fmlm = 0
stack = []
chk = 0
for i in range(n):
    if a[i] == 1: 
        if not stack: chk = i
        stack.append(1)
    else:
        stack.pop()
        if not stack and (i-chk+1) > mlm:
            fmlm = chk+1
            mlm = i-chk+1
    if len(stack) > nd and a[i] == 1:
        nd = max(len(stack),nd)
        fnd = i+1
print(nd,fnd,mlm,fmlm)



# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
