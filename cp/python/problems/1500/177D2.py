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
#print = sys.stdout.write
# ================= SOLUTION START =================


n,m,c = inp()
a = ints()
b = ints()
for i in range(1,m):
    b[i] += b[i-1]
for i in range(n):
    l = max(0,i-(n-m))
    r = min(i,m-1)
    add = b[r] if l==0 else (b[r]-b[l-1])
    a[i] = (a[i] + add) % c
print(*a)







# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
