from itertools import count
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
def ints(): return list(map(int, input().split()))  # list of ints
def strs(): return list(map(str, str1()))     # list of chars from a string
#print = sys.stdout.write
# ================= SOLUTION START =================

s = str1()
p = str1()
n,m = len(s),len(p)
if n < m:
    print(0)
else:
    # option 4
    lps = [0] * m
    prevLPS, i = 0,1
    while i < m:
        if p[i] == p[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        else:
            if prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
    res = i = j = 0
    while i < n:
        if s[i] == p[j]:
            if j == m-1:
                i += 1
                j = lps[j]
                res += 1
            else:
                i += 1
                j += 1
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
    print(res)

    '''
    # option 1
    res = 0
    for i in range(n-m+1):
        if s[i] != p[0]:
            continue
        if s[i:i+m] == p:
            res += 1
    print(res)
    '''
    '''
    # option 2
    dic = {}
    for i in range(n-m+1):
        if s[i:i+m] not in dic:
            dic[s[i:i+m]] = 1
            continue
        dic[s[i:i+m]] += 1
    print(dic[p] if p in dic else 0)
    '''
    '''
    # optionm 3
    res = 0
    for i in range(n-m+1):
        if s.startswith(p,i):
            res += 1
    print(res)
    '''

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
