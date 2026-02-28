import sys,os
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
int1 = lambda: int(input())
str1 = lambda: input().strip()
ints1 = lambda: list(map(int,str1()))
def inp(): return map(int,input().split())
def ints(): return list(map(int,input().split()))
def strs(): return list(map(str,str1()))
def mint(): return map(int,input().split())
def grid(n): return [ints() for _ in range(n)]
def grids(n): return [ints1() for _ in range(n)]
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================
def pp(n):
    d = 2
    while d * d <= n:
        if n % d == 0:
            while n % d == 0:
                n //= d
            return d if n == 1 else None
        d += 1
    return n
t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    if all(a[i]<=a[i+1] for i in range(n-1)):
        print("Bob")
        continue
    primes = []
    alice = False
    for x in a:
        p = pp(x)
        if p is None:
            alice = True
            break
        primes.append(p)
    if alice or any(primes[i] > primes[i+1] for i in range(len(primes)-1)):
        print("Alice")
    else:
        print("Bob")

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
