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
# print = sys.stdout.write
# ================= SOLUTION START =================


n,q = inp()
a = ints()  
res = 0
prefix = [0]*(n+1)
for _ in range(q):
    l,r = inp()
    prefix[l] += 1
    if (r+1)>n: continue
    prefix[r+1] -= 1
for i in range(1,n+1):
    prefix[i] = prefix[i] + prefix[i-1]
prefix.sort()
a.sort()
for i in range(n-1,-1,-1):
    res += a[i] * prefix[i+1]
print(res)





# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
