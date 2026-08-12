#!/usr/bin/env python3
from collections import defaultdict
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

n,m = inp()
world = defaultdict(list)
for _ in range(n):
    name, ctry = stp()
    world[ctry].append(name)
sub = defaultdict(int)
for _ in range(m):
    name = str1()
    sub[name] += 1
country_sub = defaultdict(int)
for ctry, chefs in world.items():
    for chef in chefs:
        country_sub[ctry] += sub[chef]
print(min(country_sub.keys(), key=lambda c:(-country_sub[c],c)))
print(min(sub.keys(), key=lambda name:(-sub[name],name)))

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
