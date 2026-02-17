import sys,os,math
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
def sgrid(n): return [input() for _ in range(n)]

# ================= SOLUTION START =================

t = int1()
for _ in range(t):
    n = int1()
    a = ints()
    gcd1,gcd2=0,0
    for i in range(n):
        if i%2==1:
	        gcd2 = math.gcd(gcd2,a[i])
        else:
            gcd1 = math.gcd(gcd1,a[i])
    flag = True
    for i in range(1,n,2):
        if a[i] % gcd1 == 0:
            flag = False
            break
    if flag:
        print(gcd1)    
        continue
    flag = True
    for i in range(0,n,2):
        if a[i]%gcd2 == 0:
            flag = False
            break
    if flag:
        print(gcd2)
    else:
        print(0)


    

# ================== SOLUTION END ==================

if LOCAL:
    sys.stdout.flush()
