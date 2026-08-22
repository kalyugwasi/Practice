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


n,m = inp()
mat = []
diff = [[0]*(m+2) for _ in range(n+2)]
for _ in range(n):
    mat.append(strs())

q = int1()
for _ in range(q):
    x1,y1,x2,y2 = inp()
    diff[x1][y1] += 1
    diff[x1][y2+1] -= 1
    diff[x2+1][y1] -= 1
    diff[x2+1][y2+1] += 1

for r in range(1,n+1):
    for c in range(1,m+1):
        diff[r][c] += diff[r-1][c] + diff[r][c-1] - diff[r-1][c-1]

for r in range(n):
    for c in range(m):
        if diff[r+1][c+1]%2==0:
            continue
        mat[r][c] = "1" if mat[r][c] == "0" else "0"

for i in range(n):
    print("".join(mat[i]))





# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
