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

n,m,k = inp()
a = ints()
diff = [0]*(n+1)
op = [0]
for _ in range(m):
    l,r,d = inp()
    op.append((l,r,d))
op_diff = [0]*(m+1)
for _ in range(k):
    x,y = inp()
    op_diff[x] += 1
    if (y+1) > m: continue
    op_diff[y+1] -= 1
for i in range(1,m+1):
    op_diff[i] += op_diff[i-1]
for i in range(1,m+1):
    l,r,d = op[i]
    diff[l] += d * op_diff[i]
    if (r+1)>n: continue
    diff[r+1] -= d * op_diff[i]
for i in range(1,n+1):
    diff[i] += diff[i-1]
for i in range(n):
    a[i] += diff[i+1]
print(*a)

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
