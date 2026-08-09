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
def ints(): return list(map(int, input().split()))  # list of ints
def strs(): return list(map(str, str1()))     # list of chars from a string

# ================= SOLUTION START =================

a = strs()
possible = 0
mid = ""
letters = list(set(a))
for i in letters:
    if a.count(i)%2 != 0:
        mid = i
        possible += 1
if possible > 1:
    print("NO SOLUTION")
    exit()
res = []
for l in letters:
    if l != mid: res += [l] * (a.count(l)//2)
if a.count(mid) > 1:
    res += [mid] * (a.count(mid)//2)
print("".join(res)+mid+"".join(res[::-1]))

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
