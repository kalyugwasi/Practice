#!/usr/bin/env python3
import sys, os
from collections import deque, defaultdict
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

"""for _ in range(int1()):
    n,k = inp()
    a = ints()
    q = deque()
    out = 0
    for i in range(n):
        p = set(q)
        out = max(out,len(q))
        if a[i] not in p and len(p)+1 >= k:
            while (set(q)) == p:
                q.popleft()
        q.append(a[i])
    out = max(out,len(q))
    print(out)"""

for _ in range(int1()):
    n, k = inp()
    a = ints()
    counts = defaultdict(int)
    distinct = 0
    l = 0
    out = 0
    for r in range(n):
        if counts[a[r]] == 0:
            distinct += 1
        counts[a[r]] += 1
        while distinct >= k:
            counts[a[l]] -= 1
            if counts[a[l]] == 0:
                distinct -= 1
            l += 1
        out = max(out, r - l + 1)
    print(out)


# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
