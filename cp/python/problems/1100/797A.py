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

# ================= SOLUTION START =================


def cntdiv(p):
    out = [i for i in range(p+1)]
    for i in range(2,math.isqrt(p)+1):
        if out[i] == i:
            for j in range(i*i,p+1,i):
                if out[j] == j:
                    out[j] = i
    return out
n,k = inp()
out = cntdiv(100005)
factors = []
temp = n
flag = 0
while temp > 1:
    factors.append(out[temp])
    temp //= out[temp]
if len(factors) < k:
    flag = -1
res = factors[:k-1]
last = 1
for f in factors[k-1:]:
    last *= f
if flag != -1:
    print(*(res[:1]+[last]+res[1:]))
else:
    print(flag)




# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()

# cfjudge
# python run.py
