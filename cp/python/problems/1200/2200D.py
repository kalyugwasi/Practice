import sys, os

def setup_io():
    try:
        base = os.path.dirname(os.path.abspath(__file__))
        judge = os.path.join(base,"..","judge")
        inpth = os.path.join(judge,"input.txt")
        outpth = os.path.join(judge,"output.txt")
        if os.path.exists(inpth):
            sys.stdin = open(inpth,"r")
            sys.stdout = open(outpth,"w")
            return True
    except:
        pass
    return False
LOCAL = setup_io()
input = sys.stdin.readline
def inp(): return map(int, input().split())
def ints(): return list(map(int, input().split()))

def min_rotation_start(s):
    s = s + s
    n = len(s)
    f = [-1] * n
    k = 0
    for j in range(1, n):
        sj = s[j]
        i = f[j - k - 1]
        while i != -1 and sj != s[k + i + 1]:
            if sj < s[k + i + 1]:
                k = j - i - 1
            i = f[i]
        if sj != s[k + i + 1]:
            if sj < s[k]:
                k = j
            f[j - k] = -1
        else:
            f[j - k] = i + 1
    return k

def z_function(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z

# ================= SOLUTION START =================
t = int(input())
for _ in range(t):
    n, x, y = inp()
    p = ints()
    mid = p[x:y]
    outer = p[:x] + p[y:]
    if not mid:
        print(*outer)
        continue
    r = min_rotation_start(mid)
    R = mid[r:] + mid[:r]         
    if not outer:
        print(*R)
        continue
    z = z_function(R + [0] + outer)
    lr, lo = len(R), len(outer)
    best_k = lo
    for k in range(lo):
        ml = min(z[k + lr + 1], lr, lo - k)
        if ml == lr or (k + ml < lo and R[ml] < outer[k + ml]):
            best_k = k
            break
    print(*outer[:best_k], *R, *outer[best_k:])
# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()