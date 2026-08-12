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
print = sys.stdout.write

# ================= SOLUTION START =================

n,m = inp()
a = ints()
b = ints()
min_a = a.index(min(a))
mx_b = b.index(max(b))
for i in range(m):
    print(f'{min_a} {i}\n')
for i in range(n):
    if i == min_a:
        continue
    print(f'{i} {mx_b}\n')

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
