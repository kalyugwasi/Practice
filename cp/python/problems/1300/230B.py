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

n = int1()
a = ints()
mex = int(1e6)+1
is_prime = [True] * (mex)
is_prime[0] = is_prime[1] = False
for i in range(2,math.isqrt(mex)+1):
    if is_prime[i]:
        for j in range(i*i,mex,i):
            is_prime[j] = False
for i in a:
    r = math.isqrt(i)
    if i>3 and r*r == i and is_prime[r]:
        print('YES')
    else:
        print("NO")




# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
